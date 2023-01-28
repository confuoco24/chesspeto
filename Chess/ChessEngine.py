# This class is responsible for storing the data about the current state of a chess game.
# It will also be responsible for determining the valid moves.
# It will also keep a move log.

class GameState():
    def __init__(self):

        # board is a 8x8 2d list, each element of the list has 2 characters.
        # The first character represents the color.
        # The second character represents the piece type.
        # "--" represents a white space.

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.moveLog = []