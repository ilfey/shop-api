from fastapi import APIRouter

from models import User

router = APIRouter(prefix="/users")


@router.get(
    path="/",
    summary="Get all users"
)
def get_users() -> list[User]:
    return User.get_all()


@router.get(
    path="/{user_id}",
    summary="Get user by id",
)
def get_user(user_id: int) -> User:
    return User.get_by_id(user_id)
