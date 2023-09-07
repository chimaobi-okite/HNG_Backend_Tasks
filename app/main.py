from fastapi import FastAPI, Response, status, HTTPException
from app import schemas, utils
from datetime import datetime

app = FastAPI()


#, response_model=schemas.Information
@app.get("/", status_code=status.HTTP_200_OK)
async def get_information(slack_name:str, track:str):
    utc_time , week_day = utils.get_utc_time_day()
    print(utc_time)
    print(week_day)
    