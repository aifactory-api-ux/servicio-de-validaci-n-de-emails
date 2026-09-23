"""
Servicio de validación de emails.
Endpoint POST /validate-email para validar formato de correo electrónico.
"""

from flask import Flask, request, jsonify
import re

app = Flask(__name__)


EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def is_valid_email(email: str) -> bool:
    """
    Valida el formato de un correo electrónico usando regex compatible con RFC 5322.

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
    if not request.is_json:
        return jsonify({"error": "Content-Type debe ser application/json"}), 400

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Cuerpo de solicitud inválido"}), 400

    email = data.get('email')

    if email is None:
        return jsonify({"error": "Campo 'email' es requerido"}), 400

    if not isinstance(email, str):
        return jsonify({"error": "Campo 'email' debe ser una cadena"}), 400

    valid = is_valid_email(email)

    return jsonify({"email": email, "valid": valid}), 200


@app.route('/health', methods=['GET'])
def health():
    """
    Endpoint de salud del servicio.

    Respuesta:
        200: {"status": "ok", "service": "email-validation", "version": "1.0.0"}
    """
    return jsonify({"status": "ok", "service": "email-validation", "version": "1.0.0"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
