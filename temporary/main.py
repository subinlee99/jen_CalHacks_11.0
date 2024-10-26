from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fetchai import main
import asyncio
from pydantic import BaseModel
origins = ["*"]


# Create an instance of the FastAPI class
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,  # Allows cookies and credentials (optional)
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers (e.g., Authorization, Content-Type)
)
class Objective(BaseModel):
    objective: str = ""
# Define a root endpoint
@app.post("/call_agentverse")
async def read_root(objective: Objective):
    response = await main(objective.objective)

    return response

# Define an endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
