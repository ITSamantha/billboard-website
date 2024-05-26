import datetime
from typing import List

from fastapi import APIRouter, Depends, Request

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.routers.advertisement import ad_favourite, booking
from src.api.transformers.advertisement import AdTypeTransformer
from src.api.transformers.booking.ad_booking_available_transformer import AdBookingAvailableTransformer
from src.api.transformers.booking.booking_transformer import BookingTransformer
from src.api.transformers.review_transformer import ReviewTransformer
from src.api.transformers.worktime_transformer import WorktimeTransformer
from src.database import models
from src.database.models.entities.file import Disk, File
from src.repository.advertisement_repository import AdvertisementRepository
from src.api.transformers.advertisement.advertisement_transformer import AdvertisementTransformer

from src.database.models import Address, AdStatus, AdvertisementAdTag, AdType, Advertisement, Booking, \
    AdBookingAvailable, BookingStatus, Review, Worktime, Category, AdPhoto, User
from src.database.session_manager import db_manager

from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.storage import storage

from src.utils.validator import Validator
from src.utils.transformer import transform
from src.utils.query_params import get_params

from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy import desc, asc, func, delete, or_

import math

router = APIRouter(
    prefix="/advertisements",
    tags=["advertisements"],
)

router.include_router(ad_favourite.router)
router.include_router(booking.router)


@router.post("")
async def store(request: Request, auth: Auth = Depends()):
    """Create advertisement."""

    await auth.check_access_token(request)

    if request.state.user.available_ads == 0:
        return ApiResponse.error('Insufficient balance')

    validator = Validator(await request.json(), {
        "title": ["required", "string"],
        "user_description": ["required", "string"],
        "ad_type_id": ["required", "integer"],
        "price": ["required", "float"],
        "category_id": ["required", "integer"],
        "ad_tags": ["required", "list"],
        "ad_photos": ["required", "list"],

        # address info
        "address_id": ["nullable", "integer"],
        "city_id": ["required_without:address_id", "integer"],
        "country_id": ["required_without:address_id", "integer"],
        "street": ["required_without:address_id", "string"],
        "house": ["required_without:address_id", "string"],
        "flat": ["nullable", "string"],
        "longitude": ["nullable", "float"],
        "latitude": ["nullable", "float"]
    })

    payload = validator.validated()

    try:
        if not payload["address_id"]:
            address: Address = await AdvertisementRepository(db_manager.get_session, Address) \
                .create(validator.only(
                ["city_id", "country_id", "street", "house", "flat", "longitude", "latitude"]))
            payload["address_id"] = address.id

        advertisement: Advertisement = await SqlAlchemyRepository(db_manager.get_session, Advertisement) \
            .create(
            validator.only(["title", "user_description", "ad_type_id", "price", "category_id"]) |
            {"user_id": request.state.user.id, "ad_status_id": AdStatus.NOT_PAID,
             "address_id": payload["address_id"]})

        if len(payload["ad_tags"]) > 0:
            tags = [{"advertisement_id": advertisement.id, "ad_tag_id": ad_tag_id} for ad_tag_id in payload["ad_tags"]]
            await SqlAlchemyRepository(db_manager.get_session, AdvertisementAdTag).bulk_create(tags)

        if len(payload['ad_photos']) > 0:
            files_to_create = []
            for file in payload['ad_photos']:
                try:
                    int(file)
                except ValueError:
                    files_to_create.append(file)
                    pass

            new_file_ids = []
            for file in files_to_create:
                try:
                    file = await File.save(file)
                    new_file_ids.append(file.id)
                except Exception as e:
                    return ApiResponse.error(str(e))
            async with db_manager.get_session() as session:
                for file_id in new_file_ids:
                    session.add(AdPhoto(advertisement_id=advertisement.id, photo_id=file_id))
                await session.commit()

        await SqlAlchemyRepository(db_manager.get_session, User) \
            .update(
            data={'available_ads': request.state.user.available_ads - 1},
            id=request.state.user.id
        )

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer().include(['ad_photos'])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.put("/{advertisement_id}")
async def update(advertisement_id: int, request: Request, auth: Auth = Depends()):
    """Create advertisement."""

    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        "title": ["required", "string"],
        "user_description": ["required", "string"],
        "ad_type_id": ["required", "integer"],
        "price": ["required", "float"],
        "category_id": ["required", "integer"],
        "ad_tags": ["required", "list"],
        "ad_photos": ["required", "list"],

        # address info
        # "address_id": ["nullable", "integer"],
        # "city_id": ["required_without:address_id", "integer"],
        # "country_id": ["required_without:address_id", "integer"],
        # "street": ["required_without:address_id", "string"],
        # "house": ["required_without:address_id", "string"],
        # "flat": ["nullable", "string"],
        # "longitude": ["nullable", "float"],
        # "latitude": ["nullable", "float"]
    })

    payload = validator.validated()

    try:
        # if not payload["address_id"]:
        #     address: Address = await AdvertisementRepository(db_manager.get_session, Address) \
        #         .create(validator.only(
        #         ["city_id", "country_id", "street", "house", "flat", "longitude", "latitude"]))
        #     payload["address_id"] = address.id

        advertisement: Advertisement = await SqlAlchemyRepository(db_manager.get_session, Advertisement) \
            .get_single(id=advertisement_id)
        advertisement.title = payload['title']
        advertisement.user_description = payload['user_description']
        advertisement.ad_type_id = payload['ad_type_id']
        advertisement.price = payload['price']
        advertisement.category_id = payload['category_id']

        async with db_manager.get_session() as session:
            await session.commit()

        if len(payload["ad_tags"]) > 0:
            async with db_manager.get_session() as session:
                # bad approach.
                q = delete(AdvertisementAdTag) \
                    .filter(
                        AdvertisementAdTag.advertisement_id == advertisement.id
                    )
                await session.execute(q)
                await session.commit()
            tags = [{"advertisement_id": advertisement.id, "ad_tag_id": ad_tag_id} for ad_tag_id in payload["ad_tags"]]
            await SqlAlchemyRepository(db_manager.get_session, AdvertisementAdTag).bulk_create(tags)

        if len(payload['ad_photos']) > 0:
            file_ids_to_keep = []
            files_to_create = []
            for file in payload['ad_photos']:
                try:
                    file_ids_to_keep.append(int(file))
                except ValueError:
                    files_to_create.append(file)
                    pass

            new_file_ids = []
            for file in files_to_create:
                try:
                    file = await File.save(file)
                    new_file_ids.append(file.id)
                except Exception as e:
                    return ApiResponse.error(str(e))
            async with db_manager.get_session() as session:
                for file_id in new_file_ids:
                    session.add(AdPhoto(advertisement_id=advertisement.id, photo_id=file_id))
                await session.commit()

            async with db_manager.get_session() as session:
                q = delete(AdPhoto) \
                    .filter(
                    AdPhoto.photo_id.notin_([*file_ids_to_keep, *new_file_ids]),
                    AdPhoto.advertisement_id == advertisement.id
                )
                await session.execute(q)
                await session.commit()

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer().include(['ad_photos'])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("")
async def get_advertisements(request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)
    try:
        parsed_params = get_params(request)
        page = int(parsed_params['page']) if 'page' in parsed_params else 1
        per_page = int(parsed_params['per_page']) if 'per_page' in parsed_params else 15
        category_id = int(parsed_params['category_id']) if 'category_id' in parsed_params else None
        search = parsed_params['category_id'] if 'category_id' in parsed_params else None
        sort = parsed_params['sort'] if 'sort' in parsed_params else {}
        filters = parsed_params['filters'] if 'filters' in parsed_params else {}

        async with db_manager.get_session() as session:
            main_query = select(Advertisement)\
                .options(joinedload(Advertisement.category))
            count_query = select(func.count(Advertisement.id))

            queries = {'main': main_query, 'count': count_query}

            for key in queries.keys():
                # filtering
                if category_id:  # todo child categories
                    queries[key] = queries[key].where(Advertisement.category_id == category_id)
                # search
                if search:
                    or_clauses = []
                    for term in search.split(' '):
                        or_clauses.append(Advertisement.title.like(f"%{term}%"))
                        or_clauses.append(Advertisement.user_description.like(f"%{term}%"))
                    queries[key] = queries[key].filter(or_(*or_clauses))
                # sorting
                for col_name in sort:
                    col = getattr(Advertisement, col_name)
                    queries[key] = queries[key].order_by(asc(col) if sort[col_name] else desc(col))
                # paginating
                queries[key] = queries[key].limit(per_page)
                queries[key] = queries[key].offset(per_page * (page - 1))

            main_query, count_query = queries['main'], queries['count']

            res = await session.execute(main_query)
            advertisements = res.unique().scalars().all()

            # count_query = select(func.count(Advertisement.id))
            #
            # if category_id:  # todo child categories
            #     count_query = count_query.where(Advertisement.category_id == category_id)
            #
            # if search:
            #     or_clauses = []
            #     for term in search.split(' '):
            #         or_clauses.append(Advertisement.title.like(f"%{term}%"))
            #         or_clauses.append(Advertisement.user_description.like(f"%{term}%"))
            #     count_query = count_query.filter(or_(*or_clauses))

            count = await session.execute(count_query)
            advertisements_count = count.scalar()
            pages_total = math.ceil(advertisements_count / per_page)
        return ApiResponse.paginated(transform(
            advertisements,

            AdvertisementTransformer().include([
                'address', 'user', 'ad_tags',
                'ad_photos', 'category', 'reviews'
            ])
        ), page, per_page, pages_total)

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/ad_type")
async def get_ad_types(request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)
    try:
        ad_types: List[AdType] = await SqlAlchemyRepository(db_manager.get_session, AdType).get_multi()
        return ApiResponse.payload(transform(
            ad_types,
            AdTypeTransformer()
        ))

    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/search")
async def search_advertisements(request: Request):
    try:
        parsed_params = get_params(request)
        page = int(parsed_params['page']) if 'page' in parsed_params else 1
        per_page = int(parsed_params['per_page']) if 'per_page' in parsed_params else 15
        query = parsed_params['query'] if 'query' in parsed_params else None

        advertisement: List[Advertisement] = await AdvertisementRepository(db_manager.get_session,
                                                                           Advertisement).search_multi(
            query,
            per_page, per_page * (page - 1)
        )

        if not advertisement:
            raise Exception("There is no advertisement with this data.")

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer()
                .include([
                    'address', 'user', 'ad_tags',
                    'ad_photos', 'category', 'reviews',
                ])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{advertisement_id}")
async def get_advertisement(advertisement_id: int, request: Request, short: bool = False, auth: Auth = Depends()):
    """Get exact advertisement information. """

    # await auth.check_access_token(request)
    # TODO: SHORT VERSION
    try:
        advertisement: Advertisement = await SqlAlchemyRepository(db_manager.get_session, Advertisement).get_single(
            id=advertisement_id)

        if not advertisement:
            raise Exception("There is no advertisement with this data.")

        return ApiResponse.payload(
            transform(
                advertisement,
                AdvertisementTransformer()
                .include([
                    'address', 'user', 'ad_tags',
                    'ad_photos', 'category', 'reviews',
                ])
            )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get(path='/{advertisement_id}/reviews')
async def get_advertisement_reviews(advertisement_id: int, request: Request, auth: Auth = Depends()):
    """Get all reviews for exact advertisement. """
    await auth.check_access_token(request)
    try:
        reviews: List[Review] = await SqlAlchemyRepository(db_manager.get_session, Review).get_multi(
            advertisement_id=advertisement_id, deleted_at=None)

        return ApiResponse.payload(transform(
            reviews,
            ReviewTransformer()
        ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get(path='/{advertisement_id}/bookings')
async def get_advertisement_bookings(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:

        bookings: List[Booking] = await SqlAlchemyRepository(db_manager.get_session, Booking).get_multi(
            advertisement_id=advertisement_id, deleted_at=None)

        return ApiResponse.payload(transform(bookings,
                                             BookingTransformer()
                                             ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get(path='/{advertisement_id}/bookings_available')
async def get_advertisement_bookings_available(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:

        available_bookings: List[AdBookingAvailable] = await SqlAlchemyRepository(db_manager.get_session,
                                                                                  AdBookingAvailable).get_multi(
            advertisement_id=advertisement_id, deleted_at=None)

        return ApiResponse.payload(transform(available_bookings,
                                             AdBookingAvailableTransformer()
                                             ))
    except Exception as e:
        return ApiResponse.error(str(e))


@router.get("/{advertisement_id}/worktimes")
async def get_advertisement_worktime(advertisement_id: int, request: Request, auth: Auth = Depends()):
    # await auth.check_access_token(request)
    try:
        worktimes: List[Worktime] = await SqlAlchemyRepository(db_manager.get_session, Worktime).get_multi(
            advertisement_id=advertisement_id)

        return ApiResponse.payload(transform(
            worktimes,
            WorktimeTransformer()
        ))

    except Exception as e:
        return ApiResponse.error(str(e))


@router.post("/{advertisement_id}/bookings")
async def create_advertisement_booking(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    validator = Validator(await request.json(), {
        # 'advertisement_id': ['required', 'integer'],
        'time_from': ['required', 'string'],
        'time_end': ['required', 'string'],
        # 'time_from': ['required', 'datetime'],
        # 'time_end': ['required', 'datetime'],
        # 'deadline_at': ['required', 'datetime']
        'deadline_at': ['required', 'string'],
        'guest_count': ['required', 'integer']
    })

    validator.validated()

    validator.validated_data["time_from"] = datetime.datetime.strptime(validator.validated_data["time_from"],
                                                                       '%Y-%m-%d %H:%M:%S')

    validator.validated_data["time_end"] = datetime.datetime.strptime(validator.validated_data["time_end"],
                                                                      '%Y-%m-%d %H:%M:%S')

    validator.validated_data["deadline_at"] = datetime.datetime.strptime(validator.validated_data["deadline_at"],
                                                                         '%Y-%m-%d %H:%M:%S')

    try:
        booking: Booking = await SqlAlchemyRepository(db_manager.get_session,
                                                      Booking) \
            .create(validator.all() | {"user_id": request.state.user.id, "booking_status_id": BookingStatus.NOT_PAID,
                                       "advertisement_id": advertisement_id})

        # CHECK TYPE
        # DELETE FROM AD_BOOKING_AVAILABLE
        # TODO: ABLE TO RESTORE IF BOOKING IS CANCELLED
        # TODO: CALCULATE AVAILABLE DATES

        return ApiResponse.payload(
            transform(booking,
                      BookingTransformer()
                      )
        )
    except Exception as e:
        return ApiResponse.error(str(e))


@router.delete("/{advertisement_id}")
async def delete_advertisement(advertisement_id: int, request: Request, auth: Auth = Depends()):
    await auth.check_access_token(request)

    try:
        advertisement: Advertisement = await AdvertisementRepository(db_manager.get_session, models.Advertisement) \
            .update(data={"deleted_at": datetime.datetime.now()}, id=advertisement_id)

        return ApiResponse.payload({"advertisement_id": advertisement.id})
    except Exception as e:
        return ApiResponse.error(str(e))
