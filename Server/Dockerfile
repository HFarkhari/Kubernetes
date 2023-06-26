# Stage 1: Build stage
FROM python:3.11.4-alpine3.18 AS builder

# Install build dependencies
RUN apk add --no-cache build-base

# Install and compile pyzmq
RUN pip install --no-cache-dir pyzmq

# Stage 2: Final stage
FROM python:3.11.4-alpine3.18

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8
# its important to show print outputs as logs in kubernetes 
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# Create a non-root user
RUN addgroup -S user && adduser -S -G user user

# Copy compiled pyzmq from the builder stage
COPY --from=builder --chown=user:user /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copy zmqclient.py
COPY --chown=user:user zmqserver.py /tmp/zmqserver.py

# Set the working directory
WORKDIR /tmp

# Zmq Sub Server
EXPOSE 5555

# Switch to the non-root user
USER user

CMD ["python3", "zmqserver.py"]


