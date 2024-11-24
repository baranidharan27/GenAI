# Docker Setup
Containerize the app with Docker for easy deployment.

## Steps:
1. **Create a Dockerfile:**
```sh
   dockerfile
   FROM python:3.9-slim
```
```bash
   WORKDIR /app
   COPY requirements.txt requirements.txt
   COPY . .
   RUN pip install --no-cache-dir -r requirements.txt
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```
2.**Build and Run the Docker Image:**

```sh
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```