import pytest
from config.database import DATABASE_URL
from fastapi import status
from services.spatial_locations import (SpatialLocationService, read_locations,
                                        read_locations_by_orgid)
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker


@pytest.fixture
def database_session():
    engine = create_engine(DATABASE_URL)
    return sessionmaker(bind=engine)


def test_read_database(database_session):
    result_query = SpatialLocationService(database_session()).get_locations()
    assert len(result_query) > 0


def test_json_serializable_get_all():
    result_query = read_locations()
    assert isinstance(result_query["content"], list)
    assert len(result_query["content"]) == 19


def test_json_serializable_get_byorgid():
    result_query = read_locations_by_orgid(orgid=1)
    assert isinstance(result_query["content"], list)
    assert len(result_query["content"]) == 1


def test_json_serializable_get_byorgid_bad_request() -> None:
    result_query = read_locations_by_orgid(orgid="ERROR")
    assert result_query["status_code"] == status.HTTP_400_BAD_REQUEST
