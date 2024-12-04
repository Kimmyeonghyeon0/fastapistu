from fastapi import APIRouter

router = APIRouter(prefix="/item", tags=["item"])


@router.get("")
def get_items_handler():
    return [
        {"id": 1, "name": "iphone"}
    ]
