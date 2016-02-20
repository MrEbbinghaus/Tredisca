package me.ebbinghaus.Tredisca;

import me.ebbinghaus.Tredisca.Pieces.Piece;

import java.util.HashMap;

public class Board {
    HashMap<Vector3d, AtkBoard> atkBoards = new HashMap<>();
    private Piece[][][] board = new Piece[6][10][6];

    public Board() {
        //TODO init Board with standard layout
    }

    public Board(Piece... pieces) {
        addAll(pieces);
    }

    public void moveAtkBoard(Vector3d origin, Vector3d dest) {
        if (atkBoards.get(origin) != null && atkBoards.get(dest) == null) {

        } else {
            //Error
            //
        }
    }

    /**
     * pretty prints the board
     * for debug purposes //TODO a lot of print calls are stupid!
     */
    public void pPrint() {
        System.out.printf("%c%c    %c%c     0\n", getIcon(0, 0, 1), getIcon(1, 0, 1), getIcon(4, 0, 1), getIcon(5, 0, 1));
        System.out.printf("%c%c    %c%c     1\n", getIcon(0, 1, 1), getIcon(1, 1, 1), getIcon(4, 1, 1), getIcon(5, 1, 1));
        System.out.printf("  %c%c%c%c       1\n", getIcon(1, 1, 0), getIcon(2, 1, 0), getIcon(3, 1, 0), getIcon(4, 1, 0));
        System.out.printf("  %c%c%c%c       2\n", getIcon(1, 2, 0), getIcon(2, 2, 0), getIcon(3, 2, 0), getIcon(4, 2, 0));
        System.out.printf("  %c%c%c%c       3\n", getIcon(1, 3, 0), getIcon(2, 3, 0), getIcon(3, 3, 0), getIcon(4, 3, 0));
        System.out.printf("  %c%c%c%c       4\n", getIcon(1, 4, 0), getIcon(2, 4, 0), getIcon(3, 4, 0), getIcon(4, 4, 0));
        System.out.printf("%c%c    %c%c     4\n", getIcon(0, 4, 1), getIcon(1, 4, 1), getIcon(4, 4, 1), getIcon(5, 4, 1));
        System.out.printf("%c%c    %c%c     5\n", getIcon(0, 5, 1), getIcon(1, 5, 1), getIcon(4, 5, 1), getIcon(5, 5, 1));
        System.out.println("======");
        System.out.println("01123445");
        System.out.println("======");
        System.out.printf("%c%c    %c%c     2\n", getIcon(0, 2, 3), getIcon(1, 2, 3), getIcon(4, 2, 3), getIcon(5, 2, 3));
        System.out.printf("%c%c    %c%c     3\n", getIcon(0, 3, 3), getIcon(1, 3, 3), getIcon(4, 3, 3), getIcon(5, 3, 3));
        System.out.printf("  %c%c%c%c       3\n", getIcon(1, 3, 2), getIcon(2, 3, 2), getIcon(3, 3, 2), getIcon(4, 3, 2));
        System.out.printf("  %c%c%c%c       4\n", getIcon(1, 4, 2), getIcon(2, 4, 2), getIcon(3, 4, 2), getIcon(4, 4, 2));
        System.out.printf("  %c%c%c%c       5\n", getIcon(1, 5, 2), getIcon(2, 5, 2), getIcon(3, 5, 2), getIcon(4, 5, 2));
        System.out.printf("  %c%c%c%c       6\n", getIcon(1, 6, 2), getIcon(2, 6, 2), getIcon(3, 6, 2), getIcon(4, 6, 2));
        System.out.printf("%c%c    %c%c     6\n", getIcon(0, 6, 3), getIcon(1, 6, 3), getIcon(4, 6, 2), getIcon(5, 6, 3));
        System.out.printf("%c%c    %c%c     7\n", getIcon(0, 7, 3), getIcon(1, 7, 3), getIcon(4, 7, 2), getIcon(5, 7, 3));
        System.out.println("======");
        System.out.println("01123445");
        System.out.println("======");
        System.out.printf("%c%c    %c%c     4\n", getIcon(0, 4, 5), getIcon(1, 4, 5), getIcon(4, 4, 5), getIcon(5, 4, 5));
        System.out.printf("%c%c    %c%c     5\n", getIcon(0, 5, 5), getIcon(1, 5, 5), getIcon(4, 5, 3), getIcon(5, 5, 5));
        System.out.printf("  %c%c%c%c       5\n", getIcon(1, 5, 4), getIcon(2, 5, 4), getIcon(3, 5, 4), getIcon(4, 5, 4));
        System.out.printf("  %c%c%c%c       6\n", getIcon(1, 6, 4), getIcon(2, 6, 4), getIcon(3, 6, 4), getIcon(4, 6, 4));
        System.out.printf("  %c%c%c%c       7\n", getIcon(1, 7, 4), getIcon(2, 7, 4), getIcon(3, 7, 4), getIcon(4, 7, 4));
        System.out.printf("  %c%c%c%c       8\n", getIcon(1, 8, 4), getIcon(2, 8, 4), getIcon(3, 8, 4), getIcon(4, 8, 4));
        System.out.printf("%c%c    %c%c     8\n", getIcon(0, 8, 5), getIcon(1, 8, 5), getIcon(4, 8, 5), getIcon(5, 8, 5));
        System.out.printf("%c%c    %c%c     9\n", getIcon(0, 9, 5), getIcon(1, 9, 5), getIcon(4, 9, 5), getIcon(5, 9, 5));
    }

    public char getIcon(int x, int y, int z) {
        if (board[x][y][z] != null) {
            return board[x][y][z].getIcon();
        } else return ' ';
    }

    public Piece get(Vector3d a) {
        return board[a.x][a.y][a.z];
    }

    public void set(Vector3d dest, Piece piece) {
        board[dest.x][dest.y][dest.z] = piece;
    }

    public void move(Vector3d orig, Vector3d dest) {
        set(dest, get(orig));
        set(dest, null);
    }

    protected void addAll(Piece... pieces) {
        for (Piece piece : pieces) {
            Vector3d pos = piece.getPosition();
            board[pos.x][pos.y][pos.z] = piece;
        }
    }

    private class AtkBoard {
        private String name;
        private Vector3d pos;

        public AtkBoard(String name, Vector3d pos) {
            this.name = name;
            this.pos = pos;
        }

        public void moveAtkBoard(Vector3d dest) {
            if (atkBoards.get(dest) == null) {
                pos = dest;
                Vector3d rel = Vector3d.getRelVector(pos, dest);

                //move
                move(pos, Vector3d.add(pos, rel));
                move(pos.add(1, 0, 0), Vector3d.add(pos, rel).add(1, 0, 0));
                move(pos.add(0, 1, 0), Vector3d.add(pos, rel).add(0, 1, 0));
                move(pos.add(1, 1, 0), Vector3d.add(pos, rel).add(1, 1, 0));
            }
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public Vector3d getPos() {
            return pos;
        }

        public void setPos(Vector3d pos) {
            this.pos = pos;
        }

    }

}

