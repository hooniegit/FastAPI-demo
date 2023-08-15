from fastapi import APIRouter
from utils.curl_util import *

# test router
router = APIRouter()
@router.get("/test")
async def curl_func(cnt : int):
    return sample_util(cnt)

# curl "10.10.102.145:9000/test/?cnt=55"

# curl -X POST -H "Content-Type: application/json" -d \
#         '{"sensor_id": 1, "date":"2023-07-03", "time":"20:04:30", "gas_level": 50}' \
#         http://192.168.70.89:9000/sensor