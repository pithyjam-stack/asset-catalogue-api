from fastapi import FastAPI

app = FastAPI()

assets = []

# Endpoint 1: Test 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Endpoint 2: Get all assets
@app.get("/assets")
async def get_assets():
    return {"Asset List": assets}