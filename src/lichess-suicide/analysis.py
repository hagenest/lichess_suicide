import lichess.api
from pathlib import Path

CACHING_PATH = Path("cache/cached_games.pgn")

def get_all_lichess_games(username : str) -> Generator:
    """
    Input: lichess.org Username
    Output: All games from a Lichess user as a stream of game objects.
    Additionally cashes the files at the caching path as a single pgn file.
    """
    return lichess.api.user_games(username)

