import os

import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

INPUT_PATH = "./data/fakedata.csv"
df = pd.read_csv(INPUT_PATH, sep=";")
gdf = gpd.GeoDataFrame(
    df[["org_id", "timestamp"]],
    geometry=gpd.points_from_xy(df["longitude"], df["latitude"]),
    crs="EPSG:4326",
)
# Create a database connection
db_engine = create_engine(DATABASE_URL)

gdf.to_postgis("spatial_data", db_engine, if_exists="append", index=False)
db_engine.dispose()