from typing import List, Literal, Optional

from pydantic import BaseModel, EmailStr, StrictInt, ValidationError, conint, validator, constr
from datetime import timedelta, datetime


class Information(BaseModel):
    slack_name: str
    current_day: str
    utc_time: datetime
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: int
    