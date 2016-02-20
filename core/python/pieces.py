import utilities


class Piece:
    def __init__(self, position, color):
        self.position = position
        self.color = utilities.Color(color)
        self.unmoved = True

    def move(self, dest, board):
        if self.valid_dir(dest, board):
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

    def valid_dir(self, dest, board):
        """
        :return: True, if the destination is a valid move
        does not check if the destination is occupied
        does check if a double step is possible
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)
        print((x, y, _))

        if y is 0:
            raise utilities.InvalidMoveException("You have to go at least one step forward with your pawn!")

        if board.get_piece(dest) is None:
            raise utilities.InvalidMoveException("Your are trying to move to a invalid field!")

        if (y < 0 and self.color is utilities.Color("white")) or (y > 0 and self.color is utilities.Color("black")):
            raise utilities.InvalidMoveException("You are going in the wrong direction with your pawn!")

        if abs(x) is 0:
            if abs(y) is 1:
                if _valid_ray(self.position, dest, board):
                    return True
                else:
                    raise utilities.InvalidMoveException("Tja...")
            elif abs(y) is 2 and self.unmoved:
                if _valid_ray(self.position, dest, board):
                    return True
                else:
                    raise utilities.InvalidMoveException("Double Step not possible")
            else:
                raise utilities.InvalidMoveException("Too much exceptions")
        elif abs(x) is 1:
            if abs(y) is not 1:
                raise utilities.InvalidMoveException("abs(y) is not 1")
            if not _is_other_color(self, board.get_piece(dest)):
                raise utilities.InvalidMoveException("You can't capture your own pieces!")

        return True

    def move(self, dest, board):
        try:
            self.valid_dir(dest, board)

            board.move_piece(self.position, dest)
            if self.unmoved:
                self.unmoved = False
            self.position = dest

            print("{0} moved to {1}".format(self.name, dest))
        except utilities.InvalidMoveException:
            raise


class Knight(Piece):
    name = "Knight"
    icon = "N"

    def valid_dir(self, dest, board):
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

    def valid_dir(self, dest, board):
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

    def valid_dir(self, dest, board):
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

    def valid_dir(self, dest, board):
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

    def valid_dir(self, dest, board):
        """
        :return: True, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if castling is possible
        """
        (x, y, _) = utilities.get_rel_vector(self.position, dest)

        if (abs(x) in (0, 1)) and (abs(y) in (0, 1)):
            return True
        else:
            return False


def _is_other_color(a, b):
    if a is 0 or b is 0:
        return True

    return False if a.color is b.color else True


def _valid_ray(orig, dest, board):
    """
    :param orig: origin
    :param dest: destination
    :return: true if a nothing is on the way between the origin and the destination
    """
    (d0, d1, _) = dest
    base = utilities.get_base_vector(utilities.get_rel_vector(orig, dest))
    tmp = utilities.add_vector(orig, base)
    (t0, t1, _) = tmp

    while t0 is not d0 or t1 is not d1:
        print(tmp)
        for i in range(0, 6):
            if board.get_piece((t0, t1, i)):
                return False

            if not _is_other_color(board.get_piece(orig), board.get_piece((t0, t1, i))):
                return False

        tmp = utilities.add_vector(tmp, base)
        (t0, t1, _) = tmp

    return True
