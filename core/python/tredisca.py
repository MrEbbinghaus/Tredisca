from ast import literal_eval as make_tuple

import pieces
from utilities import InvalidMoveException
from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.init_starting_position()

    def play(self):
        print("How to play:\nExample: (x,y,z) to (x1,y1,z1)\nExample: KP0 to QP1")
        while True:
            self.board.pretty_print()
            do_move = True
            while do_move:
                (a, b) = input("White's Move:").split(" to ")
                try:
                    if a[0] in ("K", "Q"):
                        self.board.move_atk_board(a, b)
                    else:
                        self.board.move(make_tuple(a), make_tuple(b))
                    do_move = False
                except InvalidMoveException as err:
                    print(err)

            do_move = True
            self.board.pretty_print()
            while do_move:
                (a, b) = input("Black's Move:").split(" to ")
                try:
                    if a[0] in ("K", "Q"):
                        self.board.move_atk_board(a, b)
                    else:
                        self.board.move(make_tuple(a), make_tuple(b))
                    do_move = False
                except InvalidMoveException as err:
                    print(err)

    def init_starting_position(self):
        self.board.add_all((
            pieces.Rook((0, 0, 1), "white"),
            pieces.Queen((1, 0, 1), "white"),
            pieces.Pawn((0, 1, 1), "white"),
            pieces.Pawn((1, 1, 1), "white"),

            pieces.Pawn((1, 2, 0), "white"),
            pieces.Pawn((2, 2, 0), "white"),
            pieces.Pawn((3, 2, 0), "white"),
            pieces.Pawn((4, 2, 0), "white"),
            pieces.Knight((1, 1, 0), "white"),
            pieces.Bishop((2, 1, 0), "white"),
            pieces.Bishop((3, 1, 0), "white"),
            pieces.Knight((4, 1, 0), "white"),

            pieces.King((4, 0, 1), "white"),
            pieces.Rook((5, 0, 1), "white"),
            pieces.Pawn((4, 1, 1), "white"),
            pieces.Pawn((5, 1, 1), "white"),

            pieces.Rook((0, 9, 5), "black"),
            pieces.Queen((1, 9, 5), "black"),
            pieces.Pawn((0, 8, 5), "black"),
            pieces.Pawn((1, 8, 5), "black"),

            pieces.Pawn((1, 7, 4), "black"),
            pieces.Pawn((2, 7, 4), "black"),
            pieces.Pawn((3, 7, 4), "black"),
            pieces.Pawn((4, 7, 4), "black"),
            pieces.Knight((1, 8, 4), "black"),
            pieces.Bishop((2, 8, 4), "black"),
            pieces.Bishop((3, 8, 4), "black"),
            pieces.Knight((4, 8, 4), "black"),

            pieces.King((4, 9, 5), "black"),
            pieces.Rook((5, 9, 5), "black"),
            pieces.Pawn((4, 8, 5), "black"),
            pieces.Pawn((5, 8, 5), "black")
        ))


def main():
    Game().play()


if __name__ == "__main__":
    main()
