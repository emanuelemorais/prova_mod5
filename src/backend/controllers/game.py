from backend.models.game import Game
from backend.models.db import session

def get_all_games():
    games = session.query(Game).all()
    return games

def create_new_game(name, platform, price, amount):
    game = Game(name=name, platform=platform, price=price, amount=amount)
    session.add(game)
    session.commit()
    return "ok"

