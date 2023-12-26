import sqlalchemy as sa
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class SpatialData(Base):
    __tablename__ = "spatial_data"
    __table_args__ = {"schema": "public"}
    
    id = sa.Column(UUID, primary_key=True, server_default=sa.text("gen_random_uuid()"))
    timestamp = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    geometry = sa.Column(
        Geometry("GEOMETRY", srid=4326, spatial_index=True), nullable=False
    )