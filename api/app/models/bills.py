from app.extensions import db


class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    regular = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Bill {self.title} - {self.amount}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'regular': self.regular,
            'date': self.date,
        }
