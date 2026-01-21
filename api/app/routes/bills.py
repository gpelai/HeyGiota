from flask import Blueprint, request, jsonify

from app.extensions import db
from app.models import Bill
from app.utils import error, require_fields

bp = Blueprint("bills", __name__, url_prefix="/bills")

@bp.get("")
def list_bills():
    bills = Bill.query.order_by(Bill.id.desc()).all()
    return jsonify([b.to_dict() for b in bills])

@bp.get("/<int:bill_id>")
def get_bill(bill_id: int):
    bill = Bill.query.get(bill_id)
    if not bill:
        return error("Bill not found", 404)
    return jsonify(bill.to_dict())

@bp.post("")
def create_bill():
    data = request.get_json(silent=True)
    if not data:
        return error("Invalid JSON body", 400)
    
    ok, msg = require_fields(data, ["description", "value", "fixed"])
    if not ok:
        return error(msg, 400)
    
    if not isinstance(data["description"], str):
        return error("description must be a string", 400)
    if not isinstance(data["fixed"], bool):
        return error("fixed must be a boolean", 400)
    
    try:
        value = float(data["value"])

    except (TypeError, ValueError):
        return error("value must be a number", 400)
    
    bill = Bill(
        description = data["description"].strip(),
        value = value,
        fixed = data["fixed"],
    )

    db.session.add(bill)
    db.session.commit()

    return jsonify(bill.to_dict()), 201

@bp.put("/<int:bill_id>")
def update_bill(bill_id: int):
    bill = Bill.query.get(bill_id)
    
    if not bill:
        return error("Bill not found", 404)
    
    data = request.get_json(silent=True)
    if not data:
        return error("Invalid JSON body", 400)
    
    if "description" in data:
        if not isinstance(data["description"], str):
            return error("Description must be a string", 400)
        bill.description = data["description"].strip()

    if "value" in data:
        try:
            bill.value = float(data["value"])
        except(TypeError, ValueError):
            return error("Value must be a number", 400)
        
    if "fixed" in data:
        if not isinstance(data["fixed"], bool):
            return error("Fixed must be a boolean", 400)
        
    db.session.commit()
    return jsonify(bill.to_dict())

@bp.delete("/<int:bill_id>")
def delete_bill(bill_id: int):
    bill = Bill.query.get(bill_id)
    if not bill:
        return error("Bill not found", 400)
    
    db.session.delete(bill)
    db.session.commit()
    return jsonify({"deleted": True, "id": bill_id})

