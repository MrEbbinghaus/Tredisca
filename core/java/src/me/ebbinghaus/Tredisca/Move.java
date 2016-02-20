package me.ebbinghaus.Tredisca;

/**
 * Created by bjebb on 19.02.16.
 */
public class Move {
    Vector3d orig;
    Vector3d dest;

    public Move(Vector3d orig, Vector3d dest) {
        this.orig = orig;
        this.dest = dest;
    }

    public Move(String in) throws InvalidMoveException {
        parseInput(in);
    }

    private void parseInput(String in) throws InvalidMoveException {
        in = in.replaceAll("\\s", "");
        if (!in.matches("\\(\\d,\\d,\\d\\)to\\(\\d,\\d,\\d\\)"))
            throw new InvalidMoveException(in + " | is not in valid form!\nUsage: (a,b,c) to (d,e,f)");
        orig = new Vector3d(in.charAt(1) - 48, in.charAt(3) - 48, in.charAt(5) - 48);
        dest = new Vector3d(in.charAt(10) - 48, in.charAt(12) - 48, in.charAt(14) - 48);
    }

    public Vector3d getOrig() {
        return orig;
    }

    public Vector3d getDest() {
        return dest;
    }
}
