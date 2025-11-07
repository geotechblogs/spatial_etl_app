# spatial_etl_app

This task is aimed at creating an application that injects spatial data from a CSV file into a readable-friendly format (an Extract, Transform, and Load — ETL service) along with an API server that exposes the data from the storage via REST endpoints. Some of the additional requirements I wanted to add to this application are to be deployed using a docker container-like solution, and to add continous integration practices.

As you can guess from the title, this blog has two parts. First, we will create the database and ETL service in a multi-container application, and then, in a later blog, we will dive into the implementation of the API server with the CI implementation. Let's break down our project into small parts and make some draft application design.