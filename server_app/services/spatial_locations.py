from datetime import datetime

from fastapi import status

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

DUMMY_RESPONSE = [
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
  ]

def read_locations() -> dict:
    return {
        "content": DUMMY_RESPONSE,
        "status_code": status.HTTP_200_OK,
    }

def read_locations_by_orgid(orgid: int) -> dict:
    return {
        "content": DUMMY_RESPONSE,
        "status_code": status.HTTP_200_OK,
    }