from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(title="Item Management API", version="1.0.0")

# Define a Pydantic model for data validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

# In-memory storage for items
items_db: List[Item] = []
item_id_counter = 1

# TODO: Implement your endpoints here
# Task 1: Create basic endpoints
# - GET / endpoint that returns a welcome message
# - GET /items endpoint that returns a list of all items

# Task 2: Implement CRUD operations
# - POST /items to create a new item
# - PUT /items/{item_id} to update an item
# - DELETE /items/{item_id} to delete an item

# Task 3: Add validation and query parameters
# - Use Pydantic model for request validation
# - Add query parameters to GET /items for pagination

if __name__ == "__main__":
    import uvicorn
    # Run the app with: uvicorn main:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)
