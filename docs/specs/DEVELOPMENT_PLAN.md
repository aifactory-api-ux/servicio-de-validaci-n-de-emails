# DEVELOPMENT PLAN: Servicio de validación de emails

## 1. ARCHITECTURE OVERVIEW
Pequeño servicio Flask con un único endpoint POST `/validate-email` que recibe un JSON con campo `email`, valida su formato usando regex compatible con RFC 5322 y retorna el email junto con un booleano `valid`. Funciona en localhost por defecto.

## 2. ACCEPTANCE CRITERIA
1. Endpoint POST `/validate-email` acepta JSON con campo `email`
2. Retorna `{"email": "...", "valid": true/false}` según formato válido
3. Retorna 400 con `{"error": "..."}` si email falta o es inválido
4. Servidor escucha en localhost:5000

## TEAM SCOPE
- **Role:** role-be (backend_developer)

## 3. EXECUTABLE ITEMS

### ITEM 1: Implementar endpoint de validación de email
**Goal:** Crear endpoint POST /validate-email que reciba correo y devuelva si tiene formato válido

**Files to create:**
- `app.py` — Aplicación Flask con endpoint de validación
- `requirements.txt` — Dependencia Flask

**Dependencies:** Ninguna adicional (flask ya en requirements.txt)

**Validation:**
```bash
# Iniciar servidor
python app.py

# Test con email válido
curl -X POST http://localhost:5000/validate-email \
  -H "Content-Type: application/json" \
  -d '{"email": "usuario@ejemplo.com"}'
# Resultado esperada: {"email": "usuario@ejemplo.com", "valid": true}

# Test con email inválido
curl -X POST http://localhost:5000/validate-email \
  -H "Content-Type: application/json" \
  -d '{"email": "correo-invalido"}'
# Resultado esperada: {"email": "correo-invalido", "valid": false}

# Test sin campo email
curl -X POST http://localhost:5000/validate-email \
  -H "Content-Type: application/json" \
  -d '{}'
# Resultado esperada: 400 {"error": "Campo 'email' es requerido"}
```

**Role:** role-be (backend_developer)