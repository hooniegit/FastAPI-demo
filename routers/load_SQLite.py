from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_SQLite import *
from utils.curl_util import *

router = APIRouter()
@router.post('/sensor', response_class=PlainTextResponse)
async def receive_data(data_received: dict):
    SQLite_DIR = "/Users/kimdohoon/git/hooniegit/FastAPI-demo/datas/SQLite/sensors"
    return insert_measurements(data_received, SQLite_DIR)
