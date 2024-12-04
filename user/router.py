from fastapi import APIRouter, Path
from pydantic import BaseModel, Field

router = APIRouter(prefix="/users", tags=["user"])


db = [{
    "username": "sexy",
    "password": "99hyeon",
    }]


class SignUpResponse(BaseModel):
    username: str = Field(..., max_length=20, min_length=10)
    password: str

@router.post("")
def sign_up_handler(body: SignUpResponse):
    db.append({
        "username": body.username,
        "password": body.password,
    })
    return db

@router.get("/{username}")
def get_user_handler(
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            return user
    return {}

class UserUpdateResponse(BaseModel):
    password: str

@router.patch("/{username}")
def update_user_handler(
        body: UserUpdateResponse,
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            user["password"] = body.password
            return user
    return None

@router.delete("/{username}")
def delete_user_handler(
        username: str = Path(..., max_length=10),
):
    for user in db:
        if user["username"] == username:
            db.remove(user)
    return db