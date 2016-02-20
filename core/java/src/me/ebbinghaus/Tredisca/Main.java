package me.ebbinghaus.Tredisca;

import me.ebbinghaus.Tredisca.Pieces.Piece;

public class Main {
    Piece[] board = {};

    public static void main(String... args) {
        Board board = new Board();
        GameController gameController = new GameController(board);
        gameController.run();
    }
}