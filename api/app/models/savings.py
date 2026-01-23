from app.extensions import db


class Saving(db.Model):
    __tablename__ = 'savings'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    local = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Saving {self.title} - {self.amount} - {self.local}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'local': self.local,
        }
