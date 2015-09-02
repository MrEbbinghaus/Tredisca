from utilities import getRelVector

class Pawn:
    def __init__(self, position):
        self.position = position
        self.unmoved = true # needed for the double step

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does check if a double step is possible
        """
        (x, y, _) = getRelVector(self.position, dest)

        if x is 0 and y is 0:
            return false

        if (abs(x) is 1 and abs(y) is in (0, 1)) ^ \
         (abs(x) is 2 and abs(y) is 0 and self.unmoved)):
            return true
        else:
            return false

class Knight:
    def __init__(self, position):
        self.position = position

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        """
        (x, y, _) = getRelVector(self.position, dest)

        if x is 0 and y is 0:
            return false

        if (abs(x) + abs(y) is 3) and (abs(x) is not 3) and (abs(y) is not 3):
            return true
        else:
            return false

class Bishop:
    def __init__(self, position):
        self.position = position

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = getRelVector(self.position, dest)

        if x is 0 and y is 0:
            return false

        if abs(x) is abs(y):
            return true
        else:
            return false

class Rook:
    def __init__(self, position):
        self.position = position
        self.unmoved = true # needed for castling

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = getRelVector(self.position, dest)

        if (abs(x) is 0) ^ (abs(y) is 0):
            return true
        else:
            return false

class Queen:
    def __init__(self, position):
        self.position = position

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if something is in the way
        """
        (x, y, _) = getRelVector(self.position, dest)

        if x is 0 and y is 0:
            return false

        if ((abs(x) is 0) ^ (abs(y) is 0)) ^ (abs(x) is abs(y)):
            return true
        else:
            return false

class King:
    def __init__(self, position):
        self.position = position
        self.unmoved = true # needed to know if the king has already moved

    def validDir(self, dest):
        """
        returns true, if the destination is a valid move
        does not check if the destination is occupied or not on the board
        does not check if a rochade is possible
        """
        (x, y, _) = getRelVector(self.position, dest)

        if (abs(x) is in (0, 1)) and (abs(y) is in (0, 1)):
            return true
        else:
            return false