from app.extensions import db


class Investment(db.Model):
    __tablename__ = 'investments'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)
    institution = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Investment {self.description} - {self.value} - {self.institution}>'

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'institution': self.institution,
        }
