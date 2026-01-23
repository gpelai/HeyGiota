from flask import Blueprint, jsonify, request

from app.extensions import db
from app.models import Saving
from app.utils import error, require_fields

bp = Blueprint('savings', __name__, url_prefix='/savings')

@bp.get('')
def list_investments():
    savings = Saving.query.order_by(Saving.id.desc()).all()
    return jsonify([i.to_dict() for i in savings])

@bp.get('/<int:saving_id>')
def get_saving(saving_id: int):
    saving = Saving.query.get(saving_id)
    if not saving:
        return error("Save not found", 400)
    return jsonify(saving.to_dict())

@bp.post('')
def create_saving():
    data = request.get_json(silent=True)
    if not data:
        return error("Invalid JSON body", 400)
    
    ok, msg = require_fields(data, ['title', 'amount', 'local'])

    if not ok:
        return error(msg, 400)
    
    if not isinstance(data['title'], str):
        return error('Title must be a string', 400)
    if not isinstance(data['local'], str):
        return error('Local must be a string', 400)
    
    try:
        amount = float(data['title'])
    except(TypeError, ValueError):
        return error('Title must be a number', 400)
    
    item = Saving(
        title = data['title'].strip(),
        amount = amount,
        local = data['local'].strip(),
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201

@bp.put('/<int:saving_id>')
def update_saving(saving_id:int):
    item = Saving.query.get(saving_id)
    if not item:
        return error('Saving not found', 400)
    
    data = request.get_json(silent=True)
    if not data:
        return error('Invalid JSON body', 400)
    
    if 'title' in data:
        if not isinstance(data['title'], str):
            return error('Title must be a string', 400)
        item.title = data['title'].strip()

    if 'local' in data:
        if not isinstance(data['local'], str):
            return error('Local must be a string', 400)
        item.local = data['local'].strip()

    if 'amount' in data:
        try:
            item.amount = float(data['amount'])
        except(TypeError, ValueError):
            return error('Amount must be a number', 400)
        
    db.session.commit()
    return jsonify(item.to_dict())

@bp.delete('/<int:saving_id>')
def delete_saving(saving_id:int):
    item = Saving.query.get(saving_id)
    if not item:
        return error('Saving no found')
    
    db.session.delete(item)
    db.session.commit()
    return jsonify({'deleted': True, 'id': saving_id})