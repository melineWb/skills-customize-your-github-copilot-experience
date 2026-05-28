# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a modern REST API using the FastAPI framework, including creating endpoints, handling HTTP requests, managing data with path and query parameters, and validating input data using Pydantic models.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI application and create basic HTTP endpoints to understand how requests and responses work.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application instance
- Create at least two GET endpoints: one root endpoint (`/`) and one additional endpoint (e.g., `/items`)
- Return JSON responses from each endpoint
- Run the application locally using `uvicorn` and verify endpoints work using a REST client or browser
- Example response:
  ```json
  {"message": "Welcome to the API"}
  ```

### 🛠️ Build a Simple CRUD API

#### Description
Implement a complete CRUD (Create, Read, Update, Delete) API for managing a list of items stored in memory.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all items
- Implement POST endpoint to create a new item
- Implement PUT endpoint to update an existing item by ID
- Implement DELETE endpoint to remove an item by ID
- Use appropriate HTTP status codes (200, 201, 404)
- Store items in a list or dictionary (in-memory storage is acceptable)
- Example item structure:
  ```json
  {"id": 1, "name": "Item Name", "description": "Item Description"}
  ```

### 🛠️ Add Request Validation and Query Parameters

#### Description
Enhance your API with proper data validation using Pydantic models and support for flexible querying using query parameters.

#### Requirements
Completed program should:

- Define a Pydantic model to validate item structure on POST/PUT requests
- Add query parameters to the GET endpoint (e.g., `?skip=0&limit=10` for pagination)
- Return proper error responses with descriptive messages for invalid data
- Test the API with valid and invalid requests to demonstrate validation
- Example validation error:
  ```json
  {"detail": [{"loc": ["body", "name"], "msg": "field required"}]}
  ```
