from app.extensions import db
from app.models import Bill
from app.utils import error, require_fields
from flask import Blueprint, jsonify, request
import datetime

bp = Blueprint('bills', __name__, url_prefix='/bills')


@bp.get('')
def list_bills():
    bills = Bill.query.order_by(Bill.id.desc()).all()
    return jsonify([b.to_dict() for b in bills])


@bp.get('/<int:bill_id>')
def get_bill(bill_id: int):
    bill = Bill.query.get(bill_id)
    if not bill:
        return error('Bill not found', 404)
    return jsonify(bill.to_dict())


@bp.post('')
def create_bill():
    data = request.get_json(silent=True)
    if not data:
        return error('Invalid JSON body', 400)

    ok, msg = require_fields(data, ['title', 'amount', 'regular', 'date'])
    if not ok:
        return error(msg, 400)

    if not isinstance(data['title'], str):
        return error('Title must be a string', 400)
    
    try:
        amount = float(data['amount'])
    except (TypeError, ValueError):
        return error('Amount must be a number', 400)
    
    if not isinstance(data['date'], str):
        return error('Date must be a string')
    
    if not isinstance(data['regular'], bool):
        return error('Regular must be a boolean', 400)




    bill = Bill(
        title= data['title'].strip(),
        amount= amount,
        date= data['date'],
        regular= data['regular'],
    )

    db.session.add(bill)
    db.session.commit()

    return jsonify(bill.to_dict()), 201


@bp.put('/<int:bill_id>')
def update_bill(bill_id: int):
    bill = Bill.query.get(bill_id)

    if not bill:
        return error('Bill not found', 404)

    data = request.get_json(silent=True)
    if not data:
        return error('Invalid JSON body', 400)

    if 'title' in data:
        if not isinstance(data['title'], str):
            return error('Title must be a string', 400)
        bill.title = data['title'].strip()

    if 'amount' in data:
        try:
            bill.amount = float(data['amount'])
        except (TypeError, ValueError):
            return error('Amount must be a number', 400)

    if 'regular' in data:
        if not isinstance(data['regular'], bool):
            return error('Regular must be a boolean', 400)

    db.session.commit()
    return jsonify(bill.to_dict())


@bp.delete('/<int:bill_id>')
def delete_bill(bill_id: int):
    bill = Bill.query.get(bill_id)
    if not bill:
        return error('Bill not found', 400)

    db.session.delete(bill)
    db.session.commit()
    return jsonify({'deleted': True, 'id': bill_id})
