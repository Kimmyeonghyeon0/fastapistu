from fastapi import APIRouter, Path, status, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["user"])


db = [{
    "username": "sexy",
    "password": "99hyeon",
    }]


class SignUpResponse(BaseModel):
    username: str = Field(..., max_length=20, min_length=10)
    password: str

@router.post("", status_code=status.HTTP_201_CREATED)
def sign_up_handler(body: SignUpResponse):
    db.append({
        "username": body.username,
        "password": body.password,
    })
    return db

@router.get("/{username}", status_code=status.HTTP_200_OK)
def get_user_handler(
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found HaHaHaHaHaHa",
        )

class UserUpdateResponse(BaseModel):
    password: str

@router.patch("/{username}", status_code=status.HTTP_200_OK)
def update_user_handler(
        body: UserUpdateResponse,
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            user["password"] = body.password
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found HaHaHaHaHaHa",
        )

@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_handler(
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            db.remove(user)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found HaHaHaHaHaHa",
        )

