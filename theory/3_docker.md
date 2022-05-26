# Docker

After writting the Flask application, the next steps we performed in the Demo project were to package it in a Dockerfile and define a docker-compose.yml file for further usage. Those steps are vital when you wanna deploy your application locally and relevant when you want to use the pipeline.

You can use the below resources to document about defining your Dockerfile:
- [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Build your Python image](https://docs.docker.com/language/python/build-images/)

In order to build your Docker image locally, use the following:

`docker build -t <application-name>:<tag> .`

- `-t <application-name>:<tag>` flag with parameters allows you to give a name and a tag version to your image;
- `.` often forgotten, this is a very important argument! Make sure ayour current working directory is the location where your `Dockerfile` is located and by using `.` your are referencing said Dockerfile

To run a container using the built Docker image, use the following:

`docker run -d -p 8050:5001 <application-name>:<tag>`

- `-d` flag starts the container in detached mode, meaning the proccess is running in the backgroud, you will receive as output only the container id
- `-p 8050:5001` flag maps port 8050 from your local machine to port 5001 from the container


# Docker Compose

Let's spice things up a bit and also try the above operations, but this time using Docker Compose.
You can check below resources in order to write your Docker Compose file:
- [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)
- [Networking in Compose](https://docs.docker.com/compose/networking/)

In order to build your Docker image locally, using Docker Compose, use the following:

`docker-compose -f docker-compose.yml build`

- `-f docker-compose.yml` flag specifies your configuration file;
- `build` command builds the image;

To run a container using the built Docker image with Docker compose, use the following:

`docker-compose -f docker-compose.yml up`

- `up` command starts a container.

> **NOTE:** Please investigate the port mapping procedure if you want to use Docker Compose, as it is done differently than when you simply build the image locally with Docker!