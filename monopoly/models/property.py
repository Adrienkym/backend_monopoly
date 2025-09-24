from monopoly.database import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "rent": self.rent,
            "owner_id": self.owner_id
        }
