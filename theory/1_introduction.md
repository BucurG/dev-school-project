# DevOps {dev}School 2022 Final Project DEMO

## Project description

The project implements 4 HTTP RESTful methods, calls and parses the output of an API open to the internet using *Flask* framework with Python.
The application can be:
- built into a Docker image using Azure DevOps pipelines and pushed into an Azure Container Registry;
- built&deployed locally using Docker;
- built&deployed locally using Docker Compose;

## File descriptions

- Python application using *Flask* framework which:
  - implements REST API endpoints which respond to following HTTP methods: **get**, **post**, **put**, **delete**;
  - calls REST API `http://universities.hipolabs.com/search?country=United+Kingdom` and parses its output into a desired state;
- `Dockerfile` image configuration file where the code is injected with all the needed configuration;
- `docker-compose.yml` configuration file where the application is configured for ease of build and run locally;
- `azure-pipelines.yml` pipeline configuration file for building Docker image and push it to an Azure Container Registry.