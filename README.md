# Servicio de Validación de Emails

Endpoint POST `/validate-email` que valida el formato de un correo electrónico.

## Uso local

```bash
pip install -r requirements.txt
python app.py
```

El servicio estará disponible en `http://localhost:5000`.

## Endpoints

### POST /validate-email

Valida el formato de un email.

**Solicitud:**
```json
{"email": "usuario@ejemplo.com"}
```

**Respuesta exitosa (200):**
```json
{"email": "usuario@ejemplo.com", "valid": true}
```

**Respuesta de error (400):**
```json
{"error": "Campo 'email' es requerido"}
```

### GET /health

Verifica que el servicio esté activo.

**Respuesta (200):**
```json
{"status": "ok", "service": "email-validation", "version": "1.0.0"}
```

## Variables de entorno

- `FLASK_DEBUG`: Controla el modo debug (valores: true, false). Predeterminado: false