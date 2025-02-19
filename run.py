import subprocess
import os
import time

# Path to your backend and frontend directories
backend_dir = os.path.join(os.path.dirname(__file__), 'backend')
frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')

# Function to run the FastAPI backend
def run_backend():
    subprocess.Popen(['uvicorn', 'backend.app.main:app', '--reload'], cwd=backend_dir)

# Function to run the React frontend
def run_frontend():
    subprocess.Popen(['npm', 'start'], cwd=frontend_dir)

if __name__ == "__main__":
    # Run both backend and frontend in parallel
    run_backend()
    time.sleep(2)  # Give some time for the backend to initialize
    run_frontend()

    # Keep the process running to allow both servers to continue running
    try:
        while True:
            time.sleep(3600)  # Keep the process alive
    except KeyboardInterrupt:
        print("Shutting down both servers...")
