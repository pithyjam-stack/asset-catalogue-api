from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ----------------------------------------
# Models
# ----------------------------------------

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

class UpdateAsset(BaseModel):
        name : str 
        project : str = "Default"
        description : str = "None"

# Global Variables
app = FastAPI()
assets = []

# ----------------------------------------
# Helper Functions
# ----------------------------------------

# Helper function to find asset by ID
def find_asset(id: int):
    for asset in assets:
        if asset.id == id:

            return asset
    
    raise HTTPException(status_code=404, detail="Asset Not Found")

# ----------------------------------------
# API Endpoints
# ----------------------------------------

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

    full_asset = Asset(

        id = len(assets) + 1,
        version = 1,

        name = asset.name,
        asset_type = asset.asset_type,
        project = asset.project,
        description = asset.description

    )

    assets.append(full_asset)
    
    return full_asset

# Endpoint 4: Get specific asset
@app.get("/assets/{id}")
async def get_asset(id: int):

    return find_asset(id)

# Endpoint 5: Update specific asset
@app.put("/assets/{id}")
async def update_asset(id: int, update: UpdateAsset):

    asset = find_asset(id)
    asset.version += 1
    asset.name = update.name
    asset.project = update.project
    asset.description = update.description

    return asset

# Endpoint 6: Delete specific asset
@app.delete("/assets/{id}")
async def delete_asset(id: int):

    asset = find_asset(id)
    asset_name = asset.name
    assets.remove(asset)

    return {"message" : f"Asset {asset_name} has been removed."}