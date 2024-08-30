#!/bin/bash

# Navigate to the directory containing your FastAPI app
cd src/backend

# Run the FastAPI application using uvicorn
uvicorn app:app --host 0.0.0.0 --port 8508 --reload