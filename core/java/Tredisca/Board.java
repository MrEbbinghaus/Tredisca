package Tredisca;

import java.util.HashMap;

public class Board {
    HashMap<Vector3d, AtkBoard> atkBoards = new HashMap<>();
    private Piece[][][] board = new Piece[6][10][6];

    public Board() {
        //TODO init Board with standard layout
    }

    public void moveAtkBoard(String origin, String dest) {
        if (atkBoards.get(origin) != null && atkBoards.get(dest) == null) {

        } else {
            //Error
            //
        }
    }

    /**
     * pretty prints the board
     */
    public void pPrint() {
        //TODO implement
    }

    private class AtkBoard {
        private String name;
        private Vector3d pos;

        public AtkBoard(String name, Vector3d pos) {
            this.name = name;
            this.pos = pos;
        }

        public void move(Vector3d dest) {
            if (atkBoards.get(dest) == null) {

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

