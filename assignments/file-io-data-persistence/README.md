# 📘 Assignment: File I/O & Data Persistence

## 🎯 Objective

Master reading and writing different file formats in Python, including text files, CSV, and JSON. Learn to persist data beyond program execution and handle structured data effectively for real-world applications.

## 📝 Tasks

### 🛠️ Basic File Operations

#### Description
Learn how to read from and write to text files, implementing functions that manipulate file content.

#### Requirements
Completed program should:

- Implement a function to read a text file and return its contents as a string
- Implement a function to write text to a file (creating it if it doesn't exist)
- Implement a function to append new lines to an existing file
- Implement a function to read a file and return lines as a list
- Handle file operations gracefully with appropriate error handling
- Example usage:
  ```python
  write_file("log.txt", "Program started")
  append_file("log.txt", "Task completed")
  contents = read_file("log.txt")
  ```

### 🛠️ Parsing and Writing CSV Files

#### Description
Work with CSV (Comma-Separated Values) files to read tabular data and write data in CSV format.

#### Requirements
Completed program should:

- Read a CSV file and parse it into a list of dictionaries (where each row is a dictionary)
- Write a list of dictionaries to a CSV file with proper headers
- Filter CSV data based on column values
- Calculate statistics (count, sum, average) for numeric columns
- Example structure:
  ```python
  [
    {"name": "Alice", "score": 95, "grade": "A"},
    {"name": "Bob", "score": 87, "grade": "B"}
  ]
  ```

### 🛠️ Working with JSON Files

#### Description
Learn to serialize and deserialize JSON data, handling nested structures and complex data types.

#### Requirements
Completed program should:

- Read a JSON file and parse it into Python objects (dicts/lists)
- Write Python objects to a JSON file with proper formatting
- Update specific values within a JSON structure and save changes
- Validate JSON structure matches expected schema
- Handle nested objects and arrays in JSON
- Example JSON handling:
  ```python
  # Read, modify, and save
  data = load_json("config.json")
  data["settings"]["theme"] = "dark"
  save_json("config.json", data)
  ```
