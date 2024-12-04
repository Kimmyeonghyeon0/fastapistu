from unittest import result

from fastapi import FastAPI, Query, Path

from item import router as item_router
from user import router as user_router

app = FastAPI()
app.include_router(user_router.router)
app.include_router(item_router.router)


# http://127.0.0.1:8000/
@app.get("/")
def health_check_handler():
    return {"ping": "pong"}



# http://127.0.0.1/items
# def item_handler(max_price: int | None = None): 이렇게 입력해줘야 아래 주소같이랑 위에 주소같이 사용 가능
# http://127.0.0.1/items?max_price=10000
# path

