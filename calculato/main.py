# main.py

from fastapi import FastAPI, HTTPException, Query
from calculator import add, subtract, multiply, divide

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator"}

@app.get("/calculate")
def calculate(
    operation: str = Query(..., description="Operation to perform: add, subtract, multiply, divide"),
    a: float = Query(..., description="First number"),
    b: float = Query(..., description="Second number"),
):
    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }
