import pieces
from utilities import Board
from ast import literal_eval as make_tuple

def main():
    board = Board()
    initStartingPosition(board)
    #board.move((1,1,0), (2,3,2))
    #print("++++++++++++++++")
    #board.prettyPrint()
    play(board)

def initStartingPosition(board):
    board.addAll((
    pieces.Rook((0,0,1), "white"),
    pieces.Queen((1,0,1), "white"),
    pieces.Pawn((0,1,1), "white"),
    pieces.Pawn((1,1,1), "white"),

    pieces.Pawn((1,2,0), "white"),
    pieces.Pawn((2,2,0), "white"),
    pieces.Pawn((3,2,0), "white"),
    pieces.Pawn((4,2,0), "white"),
    pieces.Knight((1,1,0), "white"),
    pieces.Bishop((2,1,0), "white"),
    pieces.Bishop((3,1,0), "white"),
    pieces.Knight((4,1,0), "white"),

    pieces.King((4,0,1), "white"),
    pieces.Rook((5,0,1), "white"),
    pieces.Pawn((4,1,1), "white"),
    pieces.Pawn((5,1,1), "white"),

    pieces.Rook((0,9,5), "black"),
    pieces.Queen((1,9,5), "black"),
    pieces.Pawn((0,8,5), "black"),
    pieces.Pawn((1,8,5), "black"),

    pieces.Pawn((1,7,4), "black"),
    pieces.Pawn((2,7,4), "black"),
    pieces.Pawn((3,7,4), "black"),
    pieces.Pawn((4,7,4), "black"),
    pieces.Knight((1,8,4), "black"),
    pieces.Bishop((2,8,4), "black"),
    pieces.Bishop((3,8,4), "black"),
    pieces.Knight((4,8,4), "black"),

    pieces.King((4,9,5), "black"),
    pieces.Rook((5,9,5), "black"),
    pieces.Pawn((4,8,5), "black"),
    pieces.Pawn((5,8,5), "black")
    ))

def play(board):
    print("How to play:\nExample: (x,y,z)to(x1,y1,z1)")
    while True:
        board.prettyPrint()
        doMove = True
        while doMove:
            (a, b) = input("White's Move:").split("to")
            try:
                board.move(make_tuple(a), make_tuple(b))
                doMove = False
            except pieces.InvalidMoveException:
                print("failed!")

        while doMove:
            (a, b) = input("Black's Move:").split("to")
            try:
                board.move(make_tuple(a), make_tuple(b))
                doMove = False
            except pieces.InvalidMoveException:
                print("failed!")




if __name__ == "__main__":
    main()