import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ----------------------------------------
# SQLite
# ----------------------------------------

connection = sqlite3.connect("asset_catalogue.db")

cursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS assets(
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version_num INTEGER NOT NULL,

    asset_name TEXT NOT NULL,
    asset_type TEXT NOT NULL,
    project TEXT NOT NULL,
    description TEXT NOT NULL
)
"""

cursor.execute(sql)

connection.commit()
connection.close()

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

    connection = sqlite3.connect("asset_catalogue.db")

    cursor = connection.cursor()

    insert = """
    INSERT INTO assets ( 
    version_num,
    asset_name, 
    asset_type, 
    project, 
    description)

    VALUES(
    1,
    ?,
    ?,
    ?,
    ?
    )
    """

    cursor.execute(insert, (asset.name, asset.asset_type, asset.project, asset.description))
    asset_id = cursor.lastrowid

    connection.commit()
    connection.close()

    full_asset = Asset(

        id = asset_id,
        version = 1,

        name = asset.name,
        asset_type = asset.asset_type,
        project = asset.project,
        description = asset.description

    )
    
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