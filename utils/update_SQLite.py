from datetime import datetime
from libs.rank.rank import *
from libs.DB.SQLite import *

def insert_measurements(data_received:dict, SQLite_DIR:str):

    # cURL 센서 데이터 가공하기
    sensor_id = data_received["sensor_id"]
    date = data_received["date"]
    time = data_received["time"]
    measurement = data_received["measurement"]

    # 센서 측정값의 rank 정보 업데이트
    # rank = determine_rank(sensor_id, measurement)
    rank = "P"
    data_received["rank"] = rank

    # SQLite 파일 업데이트
    QUERY = f"""
        INSERT INTO sensor_data (sensor_id, date, time, measurement, rank)
        VALUES ({sensor_id}, '{date}', '{time}', {measurement}, '{rank}')
        """
    SQLite_UPDATE(SQLite_DIR, QUERY)

    # Flag 파일 생성
    FLAG_DIR = f"/flask_compose/datas/DONE/{sensor_id}"
    with open(f"{FLAG_DIR}/{sensor_id}&{date}&{time}&DONE", "w") as file:
        pass
    
    # cURL 결과 반환
    return(f"DATA RECEIVED {time}\n")
    