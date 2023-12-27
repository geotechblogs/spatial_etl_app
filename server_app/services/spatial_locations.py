from datetime import datetime

from config.database import session
from fastapi import status
from fastapi.encoders import jsonable_encoder
from models.spatial_locations import SpatialLocationsModel
from shapely import wkb


def format_results(query_results: any) -> dict:
    """
    Format the result of a postgis query to the location table
    and returns as a GeoJSON for geometries.
    """
    result_list = []
    for result in query_results:
        geom = wkb.loads(bytes(result.geometry.data))
        dict_result = {
            "org_id": result.org_id,
            "timestamp": result.timestamp,
            "geometry": geom.__geo_interface__,
        }
        result_list.append(dict_result)
    return result_list

class SpatialLocationService:
    def __init__(self, db) -> None:
        self.db = db

    def get_locations(self) -> list[dict]:
        result_query = self.db.query(SpatialLocationsModel).all()
        return result_query

    def get_locations_by_orgid(self, org_id: int) -> list[dict]:
        result_query = (
            self.db.query(SpatialLocationsModel)
            .filter(SpatialLocationsModel.org_id == org_id)
            .all()
        )
        return result_query

def read_locations() -> dict:
    try:
        result_query = SpatialLocationService(session()).get_locations()
        result_list = format_results(result_query)
        return {
                "content": jsonable_encoder(result_list),
                "status_code": status.HTTP_200_OK,
            }
    except Exception as error:
        return {
            "content": f"Something went wrong with error {error}",
            "status_code": status.HTTP_400_BAD_REQUEST,
        }


def read_locations_by_orgid(orgid: int) -> dict:
    try:
        result_query = SpatialLocationService(session()).get_locations_by_orgid(orgid)
        result_list = format_results(result_query)
        return {
                "content": jsonable_encoder(result_list),
                "status_code": status.HTTP_200_OK,
        }
    except Exception as error:
        return {
            "content": f"Something went wrong with error {error}",
            "status_code": status.HTTP_400_BAD_REQUEST,
        }