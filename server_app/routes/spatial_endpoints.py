from datetime import datetime

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

locations_router = APIRouter()

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

DUMMY_RESPONSE = {
  "content": [
    {
      "org_id": 1,
      "timestamp": now,
      "geometry": "any geometry",
    },
    {
      "org_id": 2,
      "timestamp": now,
      "geometry": "any geometry",
    }
  ],
  "status_code": status.HTTP_200_OK,
}

@locations_router.get(
    "/locations",
    tags=["locations"],
    response_model=list[dict],
    status_code=status.HTTP_200_OK
)
def get_locations() -> dict:
    response = DUMMY_RESPONSE
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
    response = DUMMY_RESPONSE
    return JSONResponse(
        content=response["content"], status_code=response["status_code"]
    )