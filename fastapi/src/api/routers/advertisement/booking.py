import datetime

from fastapi import APIRouter, Request, Depends

from src.api.dependencies.auth import Auth
from src.api.responses.api_response import ApiResponse
from src.api.transformers.booking.booking_transformer import BookingTransformer
from src.database.models import Booking, BookingStatus
from src.database.session_manager import db_manager
from src.repository.crud.base_crud_repository import SqlAlchemyRepository
from src.utils.transformer import transform
from src.utils.validator import Validator

router = APIRouter(
    prefix="/booking"
)



