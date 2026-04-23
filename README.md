# HNG14 Stage 2 DevOps Project

This repository contains a containerized full-stack application designed for a high-availability environment. It features a distributed architecture using FastAPI, Node.js, and Redis.

# Project Architecture
The stack consists of four primary services:
- **Frontend**: Node.js/Express application serving the user interface.
- **API**: FastAPI (Python) backend handling business logic and job creation.
- **Worker**: Background Python processor that consumes tasks from Redis.
- **Redis**: In-memory data store acting as the message broker between the API and Worker.

---

# Prerequisites

Before starting, ensure your machine has the following installed:
- **Docker**: [Install Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine.
- **Docker Compose**: Usually included with Docker Desktop; otherwise, install separately.
- **Git**: To clone the source code.

---

# Setup Instructions (From Scratch)

1. Clone the repository
Open your terminal and run:

git clone [https://github.com/darrybims/hng14-stage2-devops.git](https://github.com/darrybims/hng14-stage2-devops.git)
cd hng14-stage2-devops

2. Bring Up the Stack
Run the following command to build the images and start the containers in detached
mode:

docker compose up -d --build

3. Verify the Status

docker compose ps


# What a Successful Startup Looks Like

Container Status: All containers should show Up or Running status.
Log Verification: docker compose logs -f should show:
API: Uvicorn running on http://0.0.0.0:8000
Frontend: Frontend running on port 3000
Worker: Worker started, waiting for jobs...

Access the UI at: http://localhost:3000
