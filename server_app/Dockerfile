FROM python:3.10

WORKDIR /usr/src/app/geo_app

RUN apt-get update && apt-get install -y libpq-dev && \
    apt-get install -y --no-install-recommends gcc python3-dev

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    build-essential \
    && apt-get clean

# Set environment variables for GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip install fiona

COPY poetry.lock ./
COPY pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-ansi

COPY ./server_app/. ./server_app

WORKDIR /usr/src/app/geo_app/server_app

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]