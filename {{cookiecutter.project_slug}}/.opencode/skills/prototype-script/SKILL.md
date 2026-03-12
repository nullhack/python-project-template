---
name: prototype-script
description: Create quick and dirty scripts to validate feature outputs and data flows
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: feature-development
---
## What I do
Create rapid prototype scripts to validate that a feature concept works and produces expected outputs before implementing proper architecture.

## When to use me
Use this after feature definition to create a working proof-of-concept that demonstrates the feature's core functionality.

## Prototype Script Guidelines

### 1. Quick and Dirty Approach
- Focus on proving the concept works
- Don't worry about clean code yet
- Use hardcoded values and simple logic
- Get real data flowing through the system

### 2. Output Validation
- **API Responses**: Verify JSON structure and data
- **Web Scraping**: Check HTML parsing works
- **Function Returns**: Validate return types and values
- **File Operations**: Ensure file I/O works as expected

### 3. Script Structure
```python
#!/usr/bin/env python3
"""
Prototype script for [FEATURE_NAME]
Quick validation of core functionality
"""

# Hardcoded test data
TEST_INPUT = "example data"

def prototype_main_function():
    """Quick and dirty implementation."""
    # TODO: Replace with proper implementation
    result = "mock result"
    return result

if __name__ == "__main__":
    # Test the concept
    result = prototype_main_function()
    print(f"Result: {result}")
    print(f"Type: {type(result)}")
    
    # Validate expected output format
    assert result is not None
    print("✅ Prototype working!")
```

### 4. Common Prototype Patterns

#### API Client Prototype
```python
import requests

def test_api_call():
    """Test API endpoint quickly."""
    response = requests.get("https://api.example.com/data")
    data = response.json()
    
    # Print actual structure for analysis
    print("Response structure:")
    print(f"Status: {response.status_code}")
    print(f"Keys: {list(data.keys())}")
    print(f"Sample: {data}")
    
    return data

# Run and capture real output for later use
real_data = test_api_call()
```

#### Data Processing Prototype
```python
def process_raw_data(raw_input):
    """Quick data transformation test."""
    # Hardcoded transformation logic
    processed = raw_input.upper().strip()
    return {"processed": processed, "length": len(processed)}

# Test with real examples
test_cases = ["hello world", "  Python  ", ""]
for case in test_cases:
    result = process_raw_data(case)
    print(f"Input: '{case}' -> Output: {result}")
```

#### File Processing Prototype
```python
import json
from pathlib import Path

def parse_file_quick(file_path):
    """Test file parsing approach."""
    with open(file_path) as f:
        data = json.load(f)
    
    # Extract what we need
    important_fields = {
        "id": data.get("id"),
        "name": data.get("name"),
        "count": len(data.get("items", []))
    }
    
    return important_fields

# Test with real file
if Path("test.json").exists():
    result = parse_file_quick("test.json")
    print(f"Parsed: {result}")
```

### 5. Capture Real Examples
- Save actual API responses to files
- Document real input/output pairs
- Note edge cases discovered during testing
- Record performance characteristics

### 6. Script Location
Create prototypes in a temporary `prototypes/` directory:
```
prototypes/
├── feature_name_prototype.py
├── sample_responses/
│   ├── api_response.json
│   └── error_response.json
└── test_data/
    └── sample_input.txt
```

### 7. Transition to Production
After prototype validates the concept:
1. Extract real input/output examples
2. Document actual data structures found
3. Note any unexpected behavior
4. Use this data to inform proper implementation
5. Delete prototype once feature is complete

## Example Complete Prototype
```python
#!/usr/bin/env python3
"""
User authentication prototype - validate JWT generation works
"""
import jwt
import datetime
from pathlib import Path

# Quick test of JWT functionality
SECRET_KEY = "temp_secret_for_testing"

def prototype_create_jwt(user_email):
    """Quick JWT creation test."""
    payload = {
        "email": user_email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.utcnow()
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def prototype_verify_jwt(token):
    """Quick JWT verification test."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        return None

if __name__ == "__main__":
    # Test the flow
    test_email = "user@example.com"
    
    # Create token
    token = prototype_create_jwt(test_email)
    print(f"Generated token: {token}")
    print(f"Token type: {type(token)}")
    
    # Verify token
    payload = prototype_verify_jwt(token)
    print(f"Decoded payload: {payload}")
    
    # Save real example for later use
    example_output = {
        "input_email": test_email,
        "generated_token": token,
        "decoded_payload": payload,
        "token_length": len(token)
    }
    
    with open("jwt_prototype_results.json", "w") as f:
        import json
        json.dump(example_output, f, indent=2, default=str)
    
    print("✅ JWT prototype working! Results saved.")
```