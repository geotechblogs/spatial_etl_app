from fastapi import FastAPI
from routes.spatial_endpoints import locations_router

app = FastAPI()
app.title = "Geospatial Test Application"
app.version = "0.0.1"

app.include_router(locations_router)

@app.get("/")
async def root():
    return {"message": "Geospatial Test Application running!"}