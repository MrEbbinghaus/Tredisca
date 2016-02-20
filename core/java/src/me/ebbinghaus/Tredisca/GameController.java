package me.ebbinghaus.Tredisca;

import java.util.Scanner;

/**
 * Created by bjebb on 19.02.16.
 */
public class GameController {
    private Board board;
    private boolean whitesTurn = true;

    public GameController(Board board) {
        this.board = board;
    }

    public void run() {
        boolean running = true;
        Scanner s = new Scanner(System.in);

        while (running) {
            boolean inputCorrect;
            board.pPrint();
            do {
                inputCorrect = true;
                System.out.print((whitesTurn ? "Whites" : "Blacks") + " turn: ");

                String input = s.nextLine();
                if (input.equals("exit")) destruct();

                try {
                    Move move = new Move(input);

                } catch (InvalidMoveException e) {
                    System.out.println(e.getMessage());
                    inputCorrect = false;
                }
            } while (!inputCorrect);
            whitesTurn = !whitesTurn;
        }
    }

    protected void destruct() {
        System.out.println("Good Bye!");
        System.exit(0);
    }
}
