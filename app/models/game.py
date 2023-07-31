from app import db

class Game(db.Model): 
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    opening = db.Column(db.String)
    board_init = db.Column(db.PickleType)
    fen = db.Column(db.String)
    is_complete = db.Column(db.Boolean, default=False)
    move_list = db.Column(db.ARRAY(db.String()), default=[])

    def to_dict(self): 
        response_format = {
            "game_id" : self.game_id,
            "opening" : self.opening,
            "board_init" : self.board_init,
            "fen" : self.fen,
            "move_list" : self.move_list, 
            "is_complete": self.is_complete
        }
        return response_format
    
    @classmethod
    def from_dict(cls, game_data): 
        return cls(
            openning=game_data["opening"],
            fen=game_data["fen"],
            move_list=game_data["move_list"],
            is_complete=game_data["is_complete"]
        )