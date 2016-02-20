package me.ebbinghaus.Tredisca.Pieces;

import me.ebbinghaus.Tredisca.Board;
import me.ebbinghaus.Tredisca.InvalidMoveException;
import me.ebbinghaus.Tredisca.Move;
import me.ebbinghaus.Tredisca.Vector3d;

/**
 * Created by bjebb on 20.02.16.
 */
public class King extends Piece {

    public King(Board board, boolean color, Vector3d position) {
        super(board, color, position, color ? 'k' : 'K');
    }

    @Override
    public void move(Board board, Move move) throws InvalidMoveException {

    }
}
