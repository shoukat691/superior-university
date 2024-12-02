import math

# Define a simple game state
class GameState:
    def __init__(self, board, is_maximizing_player):
        self.board = board
        self.is_maximizing_player = is_maximizing_player

    def get_possible_moves(self):
        # This should return a list of possible moves for the current player
        # For simplicity, let's assume it returns the indices of empty spaces
        return [i for i, x in enumerate(self.board) if x is None]

    def make_move(self 