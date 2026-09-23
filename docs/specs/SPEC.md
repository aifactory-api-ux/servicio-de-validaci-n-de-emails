# SPEC.md

## 1. TECHNOLOGY STACK

- Python 3.x (standard library)
- Flask (minimal web framework for endpoint routing)

## 2. DATA CONTRACTS

**Request Payload (JSON body):**
```json
{
  "email": "string"
}
```

**Response Payload (JSON):**
```json
{
  "email": "string",
  "valid": true
}
```

**Error Response:**
```json
{
  "error": "string"
}
```

## 3. API ENDPOINTS

```
POST /validate-email
```

## 4. FILE STRUCTURE

```
├── app.py
└── requirements.txt
```

**app.py** — Flask application with email validation endpoint and regex-based format validation.

**requirements.txt** — Single line declaring Flask dependency.

## 5. ENVIRONMENT VARIABLES

`None`

## 6. IMPORT CONTRACTS

```python
from flask import Flask, request, jsonify
import re
```

**Route symbol:** `app`
**Start command:** `python app.py`

## 10. FUNCTIONAL REQUIREMENTS COVERAGE

| Requirement (source phrase) | Mapped to file(s) |
|------------------------------|-------------------|
| "crear un endpoint que reciba un correo" | app.py |
| "devuelva si tiene un formato válido" | app.py |
| "funcionando mientras local" | app.py (localhost default) |

---

**Endpoint behavior:** Accepts POST requests at `/validate-email`, extracts the `email` field from JSON body, validates using RFC 5322-compatible regex, returns JSON with original email and boolean `valid` flag. Invalid or missing `email` field returns 400 with error message.