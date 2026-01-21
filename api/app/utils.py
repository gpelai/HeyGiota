from flask import jsonify

def error(message: str, status_code: int = 400):
    return jsonify({"error": message}), status_code

def require_fields(data: dict, fields: list[str]):
    missing = [f for f in fields if f not in data]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, ""