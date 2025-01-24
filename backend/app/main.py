# import sys
# import os

# # Add the src directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# # Now imports from src will work
# from backend.src.models.llm_model import LLMModel
#  # This should work now

# # backend/app/main.py
# from fastapi import FastAPI
# from .api import router  # Import the routes from api.py

# app = FastAPI()

# # Include the router to handle routes like /api/chat
# app.include_router(router)

# # FastAPI should be run with: uvicorn backend.app.main:app --reload
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# backend/app/main.py
from fastapi import FastAPI
from .api import router  # Import the API routes

app = FastAPI()

# Include the router for routes like /api/chat
app.include_router(router)

# Run with: uvicorn backend.app.main:app --reload

# Allow CORS from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend's URL like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router)

# Running the FastAPI server with: uvicorn backend.app.main:app --reload
