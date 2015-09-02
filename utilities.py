class Board:
    """
    Represents a 3D-chess board from the Star Trek series.
    """
    names = {
    4:"Rook",
    1:"Pawn",
    5:"Queen",
    6:"King",
    2:"Knight",
    3:"Bishop",
    "QL":"Queen's Level",
    "KL":"King's Level"
    }

    def __init__(self):
        self.board = [[[None for k in range(6)] for j in range(10)] for i in range(6)]
        self.atkBoards = list()
        self.pins = {
            # Just the queen's side. Add 4 to the first value to get the king's side
            # this are just the left-bottom coordinates
            0: (0,0,1),
            1: (0,4,1),
            2: (0,2,3),
            3: (0,6,3),
            4: (0,4,5),
            5: (0,8,5)}
        self.names = {
        4: ("R", "Rook"),
        1: ("P", "Pawn"),
        5: ("Q","Queen"),
        6: ("K","King"),
        2: ("N","Knight"),
        3: ("B","Bishop")
        }

        self._initMainBoards()
        self._initAtkBoards()

    def _initMainBoards(self):
        """
        Inits the three main boards
        """
        for y in range(1,5):
            #black's board
            for x in range(5,9):
                self.board[y][x][4] = 0

            #neutral board
            for x in range(3,7):
                self.board[y][x][2] = 0

            #white's board
            for x in range(1,5):
                self.board[y][x][0] = 0

    def _initAtkBoards(self):
        """
        Inits the four attack boards
        """
        for i in range(0, 2):
            for j in range(0, 2):
                # white attack boards
                self.board[i][j][1] = 0
                self.board[i+4][j][1] = 0


                # black attack boards
                self.board[i][8+j][5] = 0
                self.board[i+4][8+j][5] = 0

        self.atkBoards.append("QP0")
        self.atkBoards.append("KP0")

        self.atkBoards.append("QP5")
        self.atkBoards.append("KP5")

    def getPiece(self, orig):
        """
        returns the piece on the origin
        """
        (x, y, z) = orig
        return self.board[x][y][z]

    def setPiece(self, dest, piece):
        """
        sets the piece on the destination
        no check if destination is None or is occupied
        """
        (x, y, z) = dest
        self.board[x][y][z] = piece

    def movePiece(self, orig, dest):
        """
        moves a piece from its origin to the destination
        returns None if the destination is None
        returns the piece if the piece is None or 0
        """
        piece = self.getPiece(orig)

        if self.getPiece(dest) is None:
            return None

        if not piece is None and (not piece is 0):
            self.setPiece(dest, piece)
            self.setPiece(orig, 0)

        return self.getPiece(dest)

    def moveAtkBoard(self, orig, dest):
        """
        moves an attack board on a pin and all pieces on top of it to the new pin
        updates the usable fields
        """
        if orig not in self.atkBoards:
            return

        if dest not in self.atkBoards:
                                                                # get bottom-left field on king's side
            field = self.pins[int(orig[2])] if orig[0] == "Q" else addVector(self.pins[int(orig[2])], (4, 0, 0))

            vector = self._getRelAtkBoardVector(orig, dest)

            allOrigins = (field,
                addVector(field, (0, 1, 0)),
                addVector(field, (1, 0, 0)),
                addVector(field, (1, 1, 0))
            )

            for o in allOrigins:
                self.setPiece(addVector(o, vector), self.getPiece(o))
                self.setPiece(o, None)

            self.atkBoards.remove(orig)
            self.atkBoards.append(dest)

    def _getRelAtkBoardVector(self, atkBoard0, atkBoard1):
        """returns the vector from atkBoard1 to atkBoard2"""
        (x0, y0, z0) = self.pins[int(atkBoard0[2])]
        (x1, y1, z1) = self.pins[int(atkBoard1[2])]

        if atkBoard0[0] == "K" and atkBoard1[0] == "Q":
            x0 = x0 + 4
        elif atkBoard0[0] == "Q" and atkBoard1[0] == "K":
            x1 = x1 + 4

        return (x1-x0, y1-y0, z1-z0)

    def _getIcon(self, position):
        cell = self.getPiece(position)
        if cell is not None:
            if cell is not 0:
                if cell > 0:
                    return ""+ bcolors.OKBLUE + names[cell][0] + bcolors.ENDC
                else:
                    return ""+bcolors.WARNING + names[-cell][0] + bcolors.ENDC
            else:
                return "_"
        else:
            return " "

    def prettyPrint(self):
        print("{0}{1}    {2}{3}     0   level 1".format(self._getIcon((0,0,1)), self._getIcon((1,0,1)), self._getIcon((4,0,1)), self._getIcon((5,0,1))))
        print("{0}{1}    {2}{3}     1".format(self._getIcon((0,1,1)), self._getIcon((1,1,1)), self._getIcon((4,1,1)), self._getIcon((5,1,1))))
        print("  {0}{1}{2}{3}       1".format(self._getIcon((1,1,0)), self._getIcon((2,1,0)), self._getIcon((3,1,0)), self._getIcon((4,1,0))))
        print("  {0}{1}{2}{3}       2   level 0".format(self._getIcon((1,2,0)), self._getIcon((2,2,0)), self._getIcon((3,2,0)), self._getIcon((4,2,0))))
        print("  {0}{1}{2}{3}       3   Black's Board".format(self._getIcon((1,3,0)), self._getIcon((2,3,0)), self._getIcon((3,3,0)), self._getIcon((4,3,0))))
        print("  {0}{1}{2}{3}       4".format(self._getIcon((1,4,0)), self._getIcon((2,4,0)), self._getIcon((3,4,0)), self._getIcon((4,4,0))))
        print("{0}{1}    {2}{3}     4   level 1".format(self._getIcon((0,4,1)), self._getIcon((1,4,1)), self._getIcon((4,4,1)), self._getIcon((5,4,1))))
        print("{0}{1}    {2}{3}     5".format(self._getIcon((0,5,1)), self._getIcon((1,5,1)), self._getIcon((4,5,1)), self._getIcon((5,5,1))))
        print("========")
        print("01123445")
        print("========")
        print("{0}{1}    {2}{3}     2   level 3".format(self._getIcon((0,2,3)), self._getIcon((1,2,3)), self._getIcon((4,2,3)), self._getIcon((5,2,3))))
        print("{0}{1}    {2}{3}     3".format(self._getIcon((0,3,3)), self._getIcon((1,3,3)), self._getIcon((4,3,3)), self._getIcon((5,3,3))))
        print("  {0}{1}{2}{3}       3".format(self._getIcon((1,3,2)), self._getIcon((2,3,2)), self._getIcon((3,3,2)), self._getIcon((4,3,2))))
        print("  {0}{1}{2}{3}       4   level 2".format(self._getIcon((1,4,2)), self._getIcon((2,4,2)), self._getIcon((3,4,2)), self._getIcon((4,4,2))))
        print("  {0}{1}{2}{3}       5   Neutral Board".format(self._getIcon((1,5,2)), self._getIcon((2,5,2)), self._getIcon((3,5,2)), self._getIcon((4,5,2))))
        print("  {0}{1}{2}{3}       6".format(self._getIcon((1,6,2)), self._getIcon((2,6,2)), self._getIcon((3,6,2)), self._getIcon((4,6,2))))
        print("{0}{1}    {2}{3}     6   level 3".format(self._getIcon((0,6,3)), self._getIcon((1,6,3)), self._getIcon((4,6,3)), self._getIcon((5,6,3))))
        print("{0}{1}    {2}{3}     7".format(self._getIcon((0,7,3)), self._getIcon((1,7,3)), self._getIcon((4,7,3)), self._getIcon((5,7,3))))
        print("========")
        print("01123445")
        print("========")
        print("{0}{1}    {2}{3}     4   level 5".format(self._getIcon((0,4,5)), self._getIcon((1,4,5)), self._getIcon((4,4,5)), self._getIcon((5,4,5))))
        print("{0}{1}    {2}{3}     5".format(self._getIcon((0,5,5)), self._getIcon((1,5,5)), self._getIcon((4,5,5)), self._getIcon((5,5,5))))
        print("  {0}{1}{2}{3}       5".format(self._getIcon((1,5,4)), self._getIcon((2,5,4)), self._getIcon((3,5,4)), self._getIcon((4,5,4))))
        print("  {0}{1}{2}{3}       6   level 4".format(self._getIcon((1,6,4)), self._getIcon((2,6,4)), self._getIcon((3,6,4)), self._getIcon((4,6,4))))
        print("  {0}{1}{2}{3}       7   White's Board".format(self._getIcon((1,7,4)), self._getIcon((2,7,4)), self._getIcon((3,7,4)), self._getIcon((4,7,4))))
        print("  {0}{1}{2}{3}       8".format(self._getIcon((1,8,4)), self._getIcon((2,8,4)), self._getIcon((3,8,4)), self._getIcon((4,8,4))))
        print("{0}{1}    {2}{3}     8   level 5".format(self._getIcon((0,8,5)), self._getIcon((1,8,5)), self._getIcon((4,8,5)), self._getIcon((5,8,5))))
        print("{0}{1}    {2}{3}     9".format(self._getIcon((0,9,5)), self._getIcon((1,9,5)), self._getIcon((4,9,5)), self._getIcon((5,9,5))))

def addVector(a, b):
    (x0, y0, z0) = a
    (x1, y1, z1) = b
    return (x0+x1, y0+y1, z0+z1)