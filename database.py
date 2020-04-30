from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config as config


_host = config.HOST
_port = config.PORT
_user = config.USER
_passwd = config.PWD
_db = config.DATABASE

engine = create_engine(
    f"mysql+pymysql://{_user}:{_passwd}@{_host}:{_port}/{_db}", echo=False, pool_size=10000, max_overflow=0)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
