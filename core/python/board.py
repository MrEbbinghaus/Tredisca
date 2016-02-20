import utilities


class Board:
    """
    Represents a 3D-chess board from the Star Trek series.
    """

    def __init__(self):
        self.board = [[[None for k in range(6)] for j in range(10)] for i in range(6)]
        self.atkBoards = list()
        self.pins = {
            # Just the queen's side. Add 4 to the first value to get the king's side
            # this are just the left-bottom coordinates
            0: (0, 0, 1),
            1: (0, 4, 1),
            2: (0, 2, 3),
            3: (0, 6, 3),
            4: (0, 4, 5),
            5: (0, 8, 5)}

        self._init_main_boards()
        self._init_atk_boards()

    def _init_main_boards(self):
        """
        Inits the three main boards
        """
        for y in range(1, 5):
            # black's board
            for x in range(5, 9):
                self.board[y][x][4] = 0

            # neutral board
            for x in range(3, 7):
                self.board[y][x][2] = 0

            # white's board
            for x in range(1, 5):
                self.board[y][x][0] = 0

    def _init_atk_boards(self):
        """
        Inits the four attack boards
        """
        for i in range(0, 2):
            for j in range(0, 2):
                # white attack boards
                self.board[i][j][1] = 0
                self.board[i + 4][j][1] = 0

                # black attack boards
                self.board[i][8 + j][5] = 0
                self.board[i + 4][8 + j][5] = 0

        self.atkBoards.append("QP0")
        self.atkBoards.append("KP0")

        self.atkBoards.append("QP5")
        self.atkBoards.append("KP5")

    def add_all(self, pieces):
        for piece in pieces:
            self.add(piece)

    def add(self, piece):
        (x, y, z) = piece.position
        self.board[x][y][z] = piece

    def is_on_board(self, position) -> bool:
        """
        returns True if the position is on the Board
        """
        if self.get_piece(position) is None:
            return False
        else:
            return True

    def get_piece(self, orig):
        """
        :return: the piece on the origin
        """
        (x, y, z) = orig
        return self.board[x][y][z]

    def set_piece(self, dest, piece):
        """
        sets the piece on the destination
        no check if destination is None or is occupied
        """
        (x, y, z) = dest
        self.board[x][y][z] = piece

    def move_piece(self, orig, dest):
        """
        moves a piece from its origin to the destination
        :return: None if the destination is None
        :return: the piece if the piece is None or 0
        """
        piece = self.get_piece(orig)

        if not self.is_on_board(dest):
            return None

        if piece is not None and piece is not 0:
            self.set_piece(dest, piece)
            self.set_piece(orig, 0)

        return self.get_piece(dest)

    def move_atk_board(self, orig, dest):
        """
        moves an attack board on a pin and all pieces on top of it to the new pin
        updates the usable fields
        """
        if orig not in self.atkBoards:
            return

        if dest not in self.atkBoards:
            # get bottom-left field on king's side
            if orig[0] == "Q":
                field = self.pins[int(orig[2])]
            else:
                field = utilities.add_vector(self.pins[int(orig[2])], (4, 0, 0))

            vector = self._get_rel_atk_board_vector(orig, dest)

            all_origins = (field,
                           utilities.add_vector(field, (0, 1, 0)),
                           utilities.add_vector(field, (1, 0, 0)),
                           utilities.add_vector(field, (1, 1, 0))
                           )

            for o in all_origins:
                self.set_piece(utilities.add_vector(o, vector), self.get_piece(o))
                self.set_piece(o, None)

            self.atkBoards.remove(orig)
            self.atkBoards.append(dest)

    def move(self, orig, dest):
        piece = self.get_piece(orig)
        if piece is not None and piece is not 0:
            piece.move(dest, self)

    def _get_rel_atk_board_vector(self, atk_board_0, atk_board_1) -> tuple:
        """returns the vector from atkBoard1 to atkBoard2"""
        (x0, y0, z0) = self.pins[int(atk_board_0[2])]
        (x1, y1, z1) = self.pins[int(atk_board_1[2])]

        if atk_board_0[0] == "K" and atk_board_1[0] == "Q":
            x0 += 4
        elif atk_board_0[0] == "Q" and atk_board_1[0] == "K":
            x1 += 4

        return x1 - x0, y1 - y0, z1 - z0

    def _get_icon(self, position):
        cell = self.get_piece(position)
        if cell is not None:
            if cell is not 0:
                if cell.color.name is "white":
                    return "" + utilities.bColors.WARNING + cell.get_icon() + utilities.bColors.ENDC
                else:
                    return "" + utilities.bColors.OKBLUE + cell.get_icon() + utilities.bColors.ENDC
            else:
                return "_"
        else:
            return " "

    def pretty_print(self):
        print("{0}{1}    {2}{3}     0   level 1".format(self._get_icon((0, 0, 1)), self._get_icon((1, 0, 1)),
                                                        self._get_icon((4, 0, 1)), self._get_icon((5, 0, 1))))
        print("{0}{1}    {2}{3}     1".format(self._get_icon((0, 1, 1)), self._get_icon((1, 1, 1)),
                                              self._get_icon((4, 1, 1)), self._get_icon((5, 1, 1))))
        print("  {0}{1}{2}{3}       1".format(self._get_icon((1, 1, 0)), self._get_icon((2, 1, 0)),
                                              self._get_icon((3, 1, 0)), self._get_icon((4, 1, 0))))
        print("  {0}{1}{2}{3}       2   level 0".format(self._get_icon((1, 2, 0)), self._get_icon((2, 2, 0)),
                                                        self._get_icon((3, 2, 0)), self._get_icon((4, 2, 0))))
        print("  {0}{1}{2}{3}       3   Whites's Board".format(self._get_icon((1, 3, 0)), self._get_icon((2, 3, 0)),
                                                               self._get_icon((3, 3, 0)), self._get_icon((4, 3, 0))))
        print("  {0}{1}{2}{3}       4".format(self._get_icon((1, 4, 0)), self._get_icon((2, 4, 0)),
                                              self._get_icon((3, 4, 0)), self._get_icon((4, 4, 0))))
        print("{0}{1}    {2}{3}     4   level 1".format(self._get_icon((0, 4, 1)), self._get_icon((1, 4, 1)),
                                                        self._get_icon((4, 4, 1)), self._get_icon((5, 4, 1))))
        print("{0}{1}    {2}{3}     5".format(self._get_icon((0, 5, 1)), self._get_icon((1, 5, 1)),
                                              self._get_icon((4, 5, 1)), self._get_icon((5, 5, 1))))
        print("========")
        print("01123445")
        print("========")
        print("{0}{1}    {2}{3}     2   level 3".format(self._get_icon((0, 2, 3)), self._get_icon((1, 2, 3)), self._get_icon((4, 2, 3)), self._get_icon((5, 2, 3))))
        print("{0}{1}    {2}{3}     3".format(self._get_icon((0, 3, 3)), self._get_icon((1, 3, 3)), self._get_icon((4, 3, 3)), self._get_icon((5, 3, 3))))
        print("  {0}{1}{2}{3}       3".format(self._get_icon((1, 3, 2)), self._get_icon((2, 3, 2)), self._get_icon((3, 3, 2)), self._get_icon((4, 3, 2))))
        print("  {0}{1}{2}{3}       4   level 2".format(self._get_icon((1, 4, 2)), self._get_icon((2, 4, 2)), self._get_icon((3, 4, 2)), self._get_icon((4, 4, 2))))
        print("  {0}{1}{2}{3}       5   Neutral Board".format(self._get_icon((1, 5, 2)), self._get_icon((2, 5, 2)), self._get_icon((3, 5, 2)), self._get_icon((4, 5, 2))))
        print("  {0}{1}{2}{3}       6".format(self._get_icon((1, 6, 2)), self._get_icon((2, 6, 2)),
                                              self._get_icon((3, 6, 2)), self._get_icon((4, 6, 2))))
        print("{0}{1}    {2}{3}     6   level 3".format(self._get_icon((0, 6, 3)), self._get_icon((1, 6, 3)),
                                                        self._get_icon((4, 6, 3)), self._get_icon((5, 6, 3))))
        print("{0}{1}    {2}{3}     7".format(self._get_icon((0, 7, 3)), self._get_icon((1, 7, 3)),
                                              self._get_icon((4, 7, 3)), self._get_icon((5, 7, 3))))
        print("========")
        print("01123445")
        print("========")
        print("{0}{1}    {2}{3}     4   level 5".format(self._get_icon((0, 4, 5)), self._get_icon((1, 4, 5)), self._get_icon((4, 4, 5)), self._get_icon((5, 4, 5))))
        print("{0}{1}    {2}{3}     5".format(self._get_icon((0, 5, 5)), self._get_icon((1, 5, 5)),
                                              self._get_icon((4, 5, 5)), self._get_icon((5, 5, 5))))
        print("  {0}{1}{2}{3}       5".format(self._get_icon((1, 5, 4)), self._get_icon((2, 5, 4)),
                                              self._get_icon((3, 5, 4)), self._get_icon((4, 5, 4))))
        print("  {0}{1}{2}{3}       6   level 4".format(self._get_icon((1, 6, 4)), self._get_icon((2, 6, 4)),
                                                        self._get_icon((3, 6, 4)), self._get_icon((4, 6, 4))))
        print("  {0}{1}{2}{3}       7   Blacks's Board".format(self._get_icon((1, 7, 4)), self._get_icon((2, 7, 4)),
                                                               self._get_icon((3, 7, 4)), self._get_icon((4, 7, 4))))
        print("  {0}{1}{2}{3}       8".format(self._get_icon((1, 8, 4)), self._get_icon((2, 8, 4)),
                                              self._get_icon((3, 8, 4)), self._get_icon((4, 8, 4))))
        print("{0}{1}    {2}{3}     8   level 5".format(self._get_icon((0, 8, 5)), self._get_icon((1, 8, 5)),
                                                        self._get_icon((4, 8, 5)), self._get_icon((5, 8, 5))))
        print("{0}{1}    {2}{3}     9".format(self._get_icon((0, 9, 5)), self._get_icon((1, 9, 5)),
                                              self._get_icon((4, 9, 5)), self._get_icon((5, 9, 5))))
