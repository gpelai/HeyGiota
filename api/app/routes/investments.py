from flask import Blueprint, jsonify, request

from app.extensions import db
from app.models import Investment
from app.utils import error, require_fields

bp = Blueprint('investiments', __name__, url_prefix='/investments')

@bp.get('')
def list_investments():
    investments = Investment.query.order_by(Investment.id.desc()).all()
    return jsonify([i.to_dict() for i in investments])

@bp.get('/<int:investment_id>')
def get_investiment(investment_id: int):
    investment = Investment.query.get(investment_id)
    if not investment:
        return error("Investment not found", 400)
    return jsonify(investment.to_dict())

@bp.post('')
def create_investment():
    data = request.get_json(silent=True)
    if not data:
        return error("Invalid JSON body", 400)
    
    ok, msg = require_fields(data, ['description', 'value', 'institution'])

    if not ok:
        return error(msg, 400)
    
    if not isinstance(data['description'], str):
        return error('Description must be a string', 400)
    if not isinstance(data['institution'], str):
        return error('Institution must be a string', 400)
    
    try:
        value = float(data['value'])
    except(TypeError, ValueError):
        return error('Value must be a number', 400)
    
    item = Investment(
        description = data['description'].strip(),
        value = value,
        institution = data['institution'].strip(),
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201

@bp.put('/<int:investment_id>')
def update_investment(investment_id:int):
    item = Investment.query.get(investment_id)
    if not item:
        return error('Investment not found', 400)
    
    data = request.get_json(silent=True)
    if not data:
        return error('Invalid JSON body', 400)
    
    if 'description' in data:
        if not isinstance(data['description'], str):
            return error('Description must be a string', 400)
        item.description = data['description'].strip()

    if 'institution' in data:
        if not isinstance(data['institution'], str):
            return error('Institution must be a string', 400)
        item.institution = data['institution'].strip()

    if 'value' in data:
        try:
            item.value = float(data['value'])
        except(TypeError, ValueError):
            return error('Value must be a number', 400)
        
    db.session.commit()
    return jsonify(item.to_dict())

@bp.delete('/<int:investment_id>')
def delete_investment(investment_id:int):
    item = Investment.query.get(investment_id)
    if not item:
        return error('Investment no found')
    
    db.session.delete(item)
    db.session.commit()
    return jsonify({'deleted': True, 'id': investment_id})