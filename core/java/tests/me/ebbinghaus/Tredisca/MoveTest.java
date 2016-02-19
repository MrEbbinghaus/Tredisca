package me.ebbinghaus.Tredisca;

import org.junit.Test;

/**
 * Created by bjebb on 19.02.16.
 */
public class MoveTest {
    @Test
    public void testStringInput() throws Exception {
        Move move = new Move("(1,2,3) to (4,5,6)");
        assert move.orig.equals(1, 2, 3) : "Origin wrong!";
        assert move.dest.equals(4, 5, 6) : "Destination wrong!";
    }
}