from app.extensions import db

class Bill(db.Model):
    __tablename__ = "bills"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)
    fixed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Bill {self.description} - {self.value}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "value": self.value,
            "fixed": self.fixed,
        }
