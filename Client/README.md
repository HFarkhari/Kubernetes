# Docker Client-Server with ZMQ Image

Welcome to the GitHub repository for the Docker Client-Server with ZMQ image! This repository provides you with multiple options to access and utilize the image.

## Docker Hub Repository

You can directly access the Docker image from the following Docker Hub repository link:

[Client-Server with ZMQ on Docker Hub](https://hub.docker.com/r/hfarkhari/client_server_zmq/tags)

## Pulling the Image

To quickly use the pre-built Docker image, you can pull the specific versions using the following commands:

**Pulling the Client Version:**

```shell
docker pull hfarkhari/client_server_zmq:client_5.0
```

**Pulling the Server Version:**

```shell
docker pull hfarkhari/client_server_zmq:server_5.0
```

## Building the Docker Images

Alternatively, if you prefer to build the Docker images yourself, you can use the provided Dockerfile and the available requirement files in this repository. Simply clone this repository to your local machine and follow these steps:

1. Navigate to the cloned repository directory.

2. Build the Docker image for the client:

   ```shell
   docker build -t client_server_zmq:client  .
   ```

3. Build the Docker image for the server:

   ```shell
   docker build -t client_server_zmq:server  .
   ```

4. Once the images are built successfully, you can use them as per your requirements.

That's it! You now have the option to either pull the pre-built Docker images or build them yourself using the provided Dockerfile. Choose the method that suits your needs.

Feel free to explore the repository and leverage the Docker images for your client-server architecture with ZMQ applications. If you have any questions or encounter any issues, please don't hesitate to reach out. Happy coding!
