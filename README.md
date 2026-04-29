# fastapi-k8s-devops-project

#  FastAPI Kubernetes DevOps Project

##  Overview
This project demonstrates building and containerizing a REST API using FastAPI and Docker.

## 🧱 Tech Stack
- FastAPI
- Docker

## ⚙️ Features
- REST API endpoints:
  - `/` → Welcome message
  - `/health` → Health check
  - `/users` → Sample user data
- Swagger UI documentation
- Containerized deployment

## 🐳 Run with Docker
```bash
docker build -t fastapi-k8s-app .
docker run -p 8000:8000 fastapi-k8s-app

## 📸 API Preview
![API Screenshot](screenshot.png)

## 🐳 Docker Container Running
![Docker Screenshot](docker.png)
