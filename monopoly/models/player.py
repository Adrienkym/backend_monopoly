from monopoly.database import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Integer, default=0)
    balance = db.Column(db.Integer, default=1500)
    in_jail = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "balance": self.balance,
            "in_jail": self.in_jail
        }
