"""
Servicio de validación de emails.
Endpoint POST /validate-email para validar formato de correo electrónico.
"""

import logging
import os
import sys
from datetime import datetime, timezone

from flask import Flask, request, jsonify
import re

app = Flask(__name__)

DEBUG = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1", "yes")

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "endpoint": "%(endpoint)s", "method": "%(method)s", "status_code": %(status_code)s}',
    datefmt="%Y-%m-%dT%H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def is_valid_email(email: str) -> bool:
    """
    Valida el formato de un correo electrónico usando regex de formato básico.

    Args:
        email: Cadena con el correo a validar.

    Returns:
        True si el formato es válido, False en caso contrario.
    """
    return bool(EMAIL_REGEX.match(email))


@app.route('/validate-email', methods=['POST'])
def validate_email():
    """
    Endpoint para validar el formato de un correo electrónico.

    Solicitud:
        POST /validate-email
        Content-Type: application/json
        Body: {"email": "correo@ejemplo.com"}

    Respuestas:
        200: {"email": "...", "valid": true/false}
        400: {"error": "..."}
    """
    endpoint = request.endpoint or "/validate-email"
    method = request.method

    if not request.is_json:
        status_code = 400
        error_msg = "Content-Type debe ser application/json"
        logger.info(
            "Solicitud rechazada",
            extra={"endpoint": endpoint, "method": method, "status_code": status_code}
        )
        return jsonify({"error": error_msg}), status_code

    data = request.get_json()

    if data is None:
        status_code = 400
        error_msg = "Cuerpo de solicitud inválido"
        logger.info(
            "Solicitud rechazada",
            extra={"endpoint": endpoint, "method": method, "status_code": status_code}
        )
        return jsonify({"error": error_msg}), status_code

    email = data.get('email')

    if email is None:
        status_code = 400
        error_msg = "Campo 'email' es requerido"
        logger.info(
            "Solicitud rechazada",
            extra={"endpoint": endpoint, "method": method, "status_code": status_code}
        )
        return jsonify({"error": error_msg}), status_code

    if not isinstance(email, str):
        status_code = 400
        error_msg = "Campo 'email' debe ser una cadena"
        logger.info(
            "Solicitud rechazada",
            extra={"endpoint": endpoint, "method": method, "status_code": status_code}
        )
        return jsonify({"error": error_msg}), status_code

    valid = is_valid_email(email)

    logger.info(
        f"Email validado: {valid}",
        extra={"endpoint": endpoint, "method": method, "status_code": 200}
    )
    return jsonify({"email": email, "valid": valid}), 200


@app.route('/health', methods=['GET'])
def health():
    """
    Endpoint de salud del servicio.

    Respuesta:
        200: {"status": "ok", "service": "email-validation", "version": "1.0.0"}
    """
    logger.info(
        "Health check",
        extra={"endpoint": "/health", "method": "GET", "status_code": 200}
    )
    return jsonify({"status": "ok", "service": "email-validation", "version": "1.0.0"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)