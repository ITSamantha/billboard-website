import React, { useEffect, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import {
  addToFavorites,
  deleteAdvertisement,
  deleteFromFavorites,
  getAdvertisementById,
  getChatId
} from '../../service/dataService';
import Loader from '../Loader';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { useDispatch, useSelector } from 'react-redux';
import { fetchMyUser, selectMyUser } from '../../redux/slices/MyUserSlice';
import ReviewBlock from '../Review/ReviewBlock';
import DeleteOutlineIcon from '@mui/icons-material/DeleteOutline';
import PhotoSlider from '../PhotoSlider/PhotoSlider';
import MapWrapper from '../../pages/Map';

const AdvertisementCard = () => {
  const { id } = useParams();
  const [ad, setAd] = useState<AdInfo | null>(null);
  const user = useSelector(selectMyUser);
  const dispatch = useDispatch();
  const [isFavourite, setIsFavourite] = useState<boolean>();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      let data = await getAdvertisementById(Number(id));
      await dispatch(fetchMyUser() as any);
      setAd(data);
      if (user) {
        const isFav = user.ad_favourites.some((ad: AdInfo) => ad.id === Number(id));
        setIsFavourite(isFav);
      }
    }

    fetchData();
  }, [dispatch, id]);

  const handleFavorite = async () => {
    setIsFavourite(true);
    await addToFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleUnfavorite = async () => {
    setIsFavourite(false);
    await deleteFromFavorites(Number(id));
    await dispatch(fetchMyUser() as any);
  };

  const handleGetChatId = async () => {
    const chatId = await getChatId(ad!.user.id);
    navigate(`/chat/${chatId.id}`);
  };

  const handleDelete = async () => {
    deleteAdvertisement(ad!.id);
  };

  if (!ad) {
    return <Loader />;
  }

  return (
    <div className="AdvertisementCard">
      <div className="container">
        <div className="AdvertisementCard__Wrapper">
          <div className="AdvertisementCard__Photos">
            <PhotoSlider photos={ad.ad_photos} />
          </div>
          <div className="AdvertisementCard__Content">
            <div className="AdvertisementCard__Main">
              <h1>{ad.title}</h1>
              <div className="AdvertisementCard__Price">₪ {ad.price}</div>
            </div>

            <div className="AdvertisementCard__Tags">
              <div className="AdvertisementCard__Tags__Item">{ad.ad_type.title}</div>
              <div className="AdvertisementCard__Tags__Item">{ad.category.title}</div>
            </div>

            <p>{ad.user_description}</p>
            <div className="AdvertisementCard__Created" title={ad.created_at}>
              {ad.created_at_str}
            </div>

            <div className="AdvertisementCard__Seller">
              <h2>Seller information</h2>

              <div className="AdvertisementCard__Seller__Content">
                <Link to={`/profile/${ad.user.id}`}>
                  <div>
                    Seller: {ad.user.first_name} {ad.user.last_name}
                  </div>
                </Link>

                {isFavourite ? (
                  <div onClick={handleUnfavorite}>
                    <FavoriteIcon />
                  </div>
                ) : (
                  <div onClick={handleFavorite}>
                    <FavoriteBorderIcon />
                  </div>
                )}

                {user && user.id !== ad.user.id ? (
                  <div onClick={handleGetChatId}>Contact the seller</div>
                ) : (
                  <div onClick={handleDelete}>
                    <DeleteOutlineIcon />
                  </div>
                )}
              </div>
            </div>

            <div className="AdvertisementCard__Address">
              <h2>Address Information</h2>
              <p>
                {[
                  ad?.address?.country?.title,
                  ad?.address?.city?.title,
                  ad?.address?.street,
                  ad?.address?.house,
                  ad?.address?.flat
                ]
                  .filter((el) => el)
                  .join(', ')}
              </p>

              <MapWrapper
                points={[
                  {
                    lat: ad?.address?.latitude,
                    lng: ad?.address?.longitude
                  }
                ]}
                center={{ lat: ad?.address?.latitude || 60, lng: ad?.address?.longitude || 30 }}
              />
            </div>

            <div className="AdvertisementCard__Reviews">
              <h2>Reviews</h2>
              <ReviewBlock reviews={ad.reviews} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdvertisementCard;
