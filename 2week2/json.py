#!/usr/bin/env python3

# json.py
import json

# 1. Parse JSON - Convert from string to Python dictionary (json.loads)
json_string = '{ "name":"John", "age":30, "city":"New York"}'
python_dict = json.loads(json_string)
print(f"Parsed age from JSON: {python_dict['age']}")

# 2. Convert from Python to JSON string with advanced formatting (json.dumps)
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}]
}

# Using indent for clean spaces and sort_keys to alphabetically order keys
pretty_json = json.dumps(x, indent=4, sort_keys=True)
print("\n--- Formatted & Sorted JSON Output ---")
print(pretty_json)

# 3. Bonus: Reading your specific sample-data.json file
print("\n--- Reading sample-data.json ---")
try:
    with open("sample-data.json", "r") as file:
        data = json.load(file)
        print("Successfully read sample-data.json!")
        print(f"Top-level keys found in file: {list(data.keys())}")
except FileNotFoundError:
    print("Warning: sample-data.json not found in this specific running directory.")
