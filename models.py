from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, DateTime

ModelBase = declarative_base()


class ALARM(ModelBase):
    __tablename__ = "SOTA_Test"

    ID = Column(BigInteger, primary_key=True)
    EventID = Column(String(512))
    SourceName = Column(String(length=512))
    SourcePath = Column(String(length=512))
    SourceID = Column(String(512))
    ServerName = Column(String(length=64))
    TicksTimeStamp = Column(Integer)
    EventTimeStamp = Column(String(512))
    EventCategory = Column(String(512))
    Severity = Column(Integer)
    Priority = Column(String(512))
    State = Column(Integer)
    Quality = Column(Integer)
    Message = Column(String(512))

    def __repr__(self):
        return f"ID is: '{self.id}' \nstring_col is: '{self.string_col}'"


