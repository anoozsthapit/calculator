# FastAPI Calculator

A simple calculator API built with FastAPI. Supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Add, subtract, multiply, and divide two numbers via REST API.
- Dockerized for easy deployment.
- Includes pytest test cases.
- GitHub Actions workflow for linting with pylint.

---

## Quick Start

### Run locally with Python

1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd calculator

2. Create and activate virtual environment:

  python3 -m venv venv
  source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the FastAPI app:
  uvicorn main:app --reload
5. Open your browser at http://localhost:8000
   Swagger UI available at http://localhost:8000/docs

##Run with Docker
- Build the image:
  docker build -t fastapi-calculator .

- Run the container:
  docker run -d -p 8000:8000 fastapi-calculator
- Or use Docker Compose:
  docker-compose up --build

##Running Tests
  pytest

                                                                                                     

   
