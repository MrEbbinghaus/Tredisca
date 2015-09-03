import utilities


class Piece:
    def __init__(self, position, color):
        self.position = position
        self.color = utilities.Color(color)
        self.unmoved = True

    def move(self, dest, board):
        if self.valid_dir(dest):
            if board.move_piece(self.position, dest) is None:
                raise utilities.InvalidMoveException()

            if type(self) in (Rook, King):
                self.unmoved = False
            self.position = dest

            print("{0} moved to {1}".format(self.name, dest))
        else:
            raise utilities.InvalidMoveException()

    def get_icon(self):
        return self.icon


class Pawn(Piece):
    name = "Pawn"
    icon = "P"

    def __init__(self, position, color):
        self.position = position
        self.color = utilities.Color(color)
        self.unmoved = True  # needed for the double step

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does check if a double step is possible
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if x is 0 and y is 0:
            return False

        print((x, y, _))
        if (abs(x) in (0, 1) and abs(y) is 1) ^ \
                (abs(x) is 0 and abs(y) is 2 and self.unmoved):
            return True
        else:
            return False

    def move(self, dest, board):
        if self.valid_dir(dest):
            (x, y, _) = utilities.get_rel_vector(self.position, dest)
            if abs(x) is 1 or abs(y) is 1:
                dest_piece = board.get_piece(dest)
                if dest_piece is None or dest_piece is 0:
                    raise utilities.InvalidMoveException()

            if board.move_piece(self.position, dest) is None:
                raise utilities.InvalidMoveException()

            if self.unmoved:
                self.unmoved = False
            self.position = dest

            print("{0} moved to {1}".format(self.name, dest))
        else:
            raise utilities.InvalidMoveException()


class Knight(Piece):
    name = "Knight"
    icon = "N"

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if x is 0 and y is 0:
            return False

        if (abs(x) + abs(y) is 3) and (abs(x) is not 3) and (abs(y) is not 3):
            return True
        else:
            return False


class Bishop(Piece):
    name = "Bishop"
    icon = "B"

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if x is 0 and y is 0:
            return False

        if abs(x) is abs(y):
            return True
        else:
            return False


class Rook(Piece):
    name = "Rook"
    icon = "R"

    def __init__(self, position, color):
        self.position = position
        self.color = utilities.Color(color)
        self.unmoved = True  # needed for castling

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if (abs(x) is 0) ^ (abs(y) is 0):
            return True
        else:
            return False


class Queen(Piece):
    name = "Queen"
    icon = "Q"

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if x is 0 and y is 0:
            return False

        if ((abs(x) is 0) ^ (abs(y) is 0)) ^ (abs(x) is abs(y)):
            return True
        else:
            return False


class King(Piece):
    name = "King"
    icon = "K"

    def __init__(self, position, color):
        self.position = position
        self.color = utilities.Color(color)
        self.unmoved = True  # needed to know if the king has already moved

    def valid_dir(self, dest):
        """
        returns True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if a rochade is possible
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if (abs(x) in (0, 1)) and (abs(y) in (0, 1)):
            return True
        else:
            return False
