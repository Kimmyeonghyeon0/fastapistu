from datetime import datetime
from pydoc import describe
from unittest import result

from fastapi import FastAPI, Query, Path, UploadFile, Response
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

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

# @app.post("/images")
# def upload_images_handler(file: UploadFile):
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "file_size": file.size,
#     }

@app.get("/now")
def now_handler():
    content= f"<html><body><h1>now: {datetime.now()}</h1></body></html>"
    return HTMLResponse(content=content,)

class NowResponse(BaseModel):
    now: datetime

@app.get("/now2", response_model=NowResponse,
         description="##  설명 \n현재 시간을 반환하는 api입니다."
         )
def now_handler():
    content= {"now2": str(datetime.now())}
    return NowResponse(now=datetime.now())
