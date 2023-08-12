from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse
from utils.check_DONE_flag import *
from datetime import datetime

router = APIRouter()
@router.post('/flag-endpoint', response_class=PlainTextResponse)
async def receive_flags(
    FLAG_DIR: str = Body(...), 
    check_time: int = Body(...), 
    interval: int = Body(...)
):
    return check_flag(FLAG_DIR, check_time, interval)

@router.get("/test")
async def test():
    return {"message": "Test is successful!"}