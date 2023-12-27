import sqlalchemy as sa
from config.database import Base
from geoalchemy2 import Geometry
from sqlalchemy.sql import func


class SpatialLocationsModel(Base):
    __tablename__ = "spatial_data"
    org_id = sa.Column(sa.Integer, primary_key=True)
    timestamp = sa.Column(sa.DateTime(timezone=True), server_default=func.now())
    geometry = sa.Column(
        Geometry("GEOMETRY", srid=4326, spatial_index=True), nullable=False
    )