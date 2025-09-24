from monopoly.database import db
class GameState(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    current_turn = db.Column(db.Integer, default=0)  # player id

    def to_dict(self):
        return {
            "id": self.id,
            "current_turn": self.current_turn
        }