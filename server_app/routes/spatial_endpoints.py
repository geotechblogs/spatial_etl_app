from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from services.spatial_locations import read_locations, read_locations_by_orgid

locations_router = APIRouter()

@locations_router.get(
    "/locations",
    tags=["locations"],
    response_model=list[dict],
    status_code=status.HTTP_200_OK
)
def get_locations() -> dict:
    response = read_locations()
    return JSONResponse(
        content=response["content"], status_code=response["status_code"]
    )

@locations_router.get(
    "/locations/",
    tags=["locations"],
    response_model=list[dict],
    status_code=status.HTTP_200_OK,
)
def get_locations_by_orgid(
    orgid: int = Query(ge=1, description="orgid for locations to search.")
) -> dict:
    response = read_locations_by_orgid(orgid=orgid)
    return JSONResponse(
        content=response["content"], status_code=response["status_code"]
    )