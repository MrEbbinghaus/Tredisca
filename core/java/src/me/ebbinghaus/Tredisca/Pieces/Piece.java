package me.ebbinghaus.Tredisca.Pieces;

import me.ebbinghaus.Tredisca.Board;
import me.ebbinghaus.Tredisca.InvalidMoveException;
import me.ebbinghaus.Tredisca.Move;
import me.ebbinghaus.Tredisca.Vector3d;

public abstract class Piece {
    Board board;
    boolean unmoved;
    boolean color; //true <=> white
    char icon;
    Vector3d position;

    public Piece(Board board, boolean color, Vector3d position, char icon) {
        this.board = board;
        this.color = color;
        this.position = position;
        this.icon = icon;
        unmoved = true;
    }

    public abstract void move(Board board, Move move) throws InvalidMoveException;

    public char getIcon() {
        return icon;
    }

    public void setIcon(char icon) {
        this.icon = icon;
    }

    public boolean isUnmoved() {
        return unmoved;
    }

    public void setUnmoved(boolean unmoved) {
        this.unmoved = unmoved;
    }

    public boolean isColor() {
        return color;
    }

    public void setColor(boolean color) {
        this.color = color;
    }

    public Vector3d getPosition() {
        return position;
    }

    public void setPosition(Vector3d position) {
        this.position = position;
    }
}