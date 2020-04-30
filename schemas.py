from typing import List

from pydantic import BaseModel


class AlarmBase(BaseModel):
    EventID: str
    SourceName: str
    SourcePath: str
    SourceID: str
    ServerName: str
    TicksTimeStamp: str
    EventTimeStamp: str
    EventCategory: str
    Severity: int
    Priority: str
    State: int
    Quality: int
    Message: str


class AlarmCreate(AlarmBase):
    pass
