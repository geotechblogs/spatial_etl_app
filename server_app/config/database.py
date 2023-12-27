from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/spatial_data_db" # We will change this later after configuring the docker compose environment
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)
Base = declarative_base()