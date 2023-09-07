import os
from fastapi import FastAPI, status
from app import schemas, utils

app = FastAPI()

def get_file_paths():
    github_repo_url = utils.GITHUB_REPO_URL
    current_file_path = os.path.abspath(__file__)
    relative_path = os.path.relpath(current_file_path)
    repo_path = os.path.join(github_repo_url, "blob/main/")
    file_github_path = os.path.join(repo_path, relative_path)
    github_file_url = file_github_path.replace("\\", "/")
    return github_repo_url, github_file_url
    

@app.get("/", status_code=status.HTTP_200_OK, response_model=schemas.Information)
def get_information(slack_name:str, track:str):
    github_repo_url, github_file_url = get_file_paths()
    utc_time, current_day = utils.get_utc_time_day()
    information = schemas.Information(slack_name=slack_name, current_day=current_day, utc_time=utc_time,
                                      track=track,github_file_url=github_file_url,github_repo_url=github_repo_url, status_code=200)
    return information
  