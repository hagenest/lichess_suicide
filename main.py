#!/usr/bin/env python3

from multiprocessing.connection import wait
import random
from pathlib import Path
from time import sleep
import lichess.api


def delete_random_file():
    """Delete a random file from the entire filesystem."""
    while True:
        try:
            random_file = random.choice(list(Path('/').rglob('*')))
            random_file.unlink()
            return random_file.name
        except:
            pass


def get_amount_blunders(png):
    """Get the amount of blunders from a PGN file."""
    return len([move for move in png if move.comment and 'blunder' in move.comment])

def get_all_lichess_games(username):
    """Get all games from a Lichess user."""
    return lichess.api.user_games(username)

def get_new_games(username, games):
    """Get all new games from a Lichess user."""
    return [game for game in get_all_lichess_games(username) if game not in games]

def is_loss(png, username):
    """Check if a game is a loss."""
    if "ai" not in str(png):
        if png["status"] != "draw" and png["status"] != "timeout" and png["status"] != "stalemate" and png["status"] != "outoftime":
            if png['winner'] == 'white' and png["players"]['white']["user"]["name"] == username:
                return True
            elif png['winner'] == 'black' and png["players"]['black']["user"]["name"] == username:
                return True
def main():
    games = []
    while True:
        new_games = get_new_games('spongeboy_ahoy', games)
        games += new_games
        print(games)
        for game in new_games:
            if is_loss(game, 'spongeboy_ahoy'):
                #print("deleted something")
                print("Deleted: {}".format(delete_random_file()))
        sleep(60)

if __name__=="__main__":
    main()
