from fastapi import FastAPI
from pydantic import BaseModel

class Asset(BaseModel):
    id : int = 0
    version : int = 0

    name : str 
    asset_type : str = "None"
    project : str = "Default"
    description : str = "None"

class CreateAsset(BaseModel):
    name : str 
    asset_type : str = "None"
    project : str = "Default"
    description : str = "None"

app = FastAPI()

assets = []

# Endpoint 1: Test 
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Endpoint 2: Get all assets
@app.get("/assets")
async def get_assets():
    return assets

# Endpoint 3: Create new asset
@app.post("/assets")
async def create_asset(asset: CreateAsset):
    new_asset = CreateAsset(
        name = asset.name,
        asset_type = asset.asset_type,
        project = asset.project,
        description = asset.description
    )
    full_asset = Asset(
        id = len(assets) + 1,
        version = 1,

        name = asset.name,
        asset_type = asset.asset_type,
        project = asset.project,
        description = asset.description
    )

    assets.append(full_asset)
    
    return assets

# Endpoint 4: Get specific asset
@app.get("/assets/{id}")
async def get_asset(id: int):
    return assets[(id - 1)]