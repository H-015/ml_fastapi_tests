from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tests = []

class Test(BaseModel):
    id: int
    name: String

@app.get("/tests", response_model=List[Test])
def get_tests():
    return tests

@app.post("/tests", response_model=Test)
def create_test(test: Test):
    tests.append(test)
    return test
