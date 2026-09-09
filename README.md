# Automated Weather Data Pipeline

## Project Overview
This repository contains a fully automated, end-to-end data pipeline that extracts real-time weather data, transforms it for analytical queries, and serves it to a visualization dashboard. The entire infrastructure is containerized using Docker.
## Architecture
Orchestration: Apache Airflow - Manages and schedules the workflow dependencies.

Extraction: Python 3 - Handles HTTP requests to the Weatherstack API and parses the raw data.

Data Warehouse: PostgreSQL - Stores both the raw extracted data and the finalized analytical models.

Transformation: dbt (data build tool) - Cleans, aggregates, and transforms the raw data into analytics-ready tables directly within Postgres.

Visualization: Apache Superset - Plugs into the Postgres database to create interactive dashboards and charts.

Containerization: Docker & Docker Compose - Hosts all services in an isolated, networked environment.
```mermaid
graph LR
    subgraph Dockerized Environment
        AF((Apache Airflow))
        
        T1[Task 1: Python calls Weatherstack API<br/>& inserts raw data into PostgreSQL]
        
        T2[Task 2: dbt creates staging tables<br/>& analytical models in PostgreSQL]
        
        SS[Apache Superset<br/>Displays finalized datasets]

        AF -->|Orchestrates Pipeline| T1
        T1 -->|On Success| T2
        T2 -->|Serves Data To| SS
    end

    %% Styling
    style AF fill:#e73a3a,stroke:#fff,color:#fff
    style T1 fill:#3366ff,stroke:#fff,color:#fff
    style T2 fill:#ff694b,stroke:#fff,color:#fff
    style SS fill:#4cc8b7,stroke:#fff,color:#fff
