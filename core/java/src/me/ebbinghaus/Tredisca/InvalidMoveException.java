package me.ebbinghaus.Tredisca;

/**
 * Created by bjebb on 19.02.16.
 */
public class InvalidMoveException extends Exception {
    public InvalidMoveException() {
    }

    public InvalidMoveException(String message) {
        super(message);
    }

    public InvalidMoveException(String message, Throwable cause) {
        super(message, cause);
    }

    public InvalidMoveException(Throwable cause) {
        super(cause);
    }

    public InvalidMoveException(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace) {
        super(message, cause, enableSuppression, writableStackTrace);
    }
}
