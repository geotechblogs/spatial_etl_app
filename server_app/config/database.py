import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = os.getenv("DATABASE_PLANET_URL")
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)
Base = declarative_base()