package me.ebbinghaus.Tredisca;

import org.junit.Test;

/**
 * Created by bjebb on 18.02.16.
 */
public class Vector3dTest {

    @Test
    public void testConstructor() throws Exception {
        Vector3d v = new Vector3d(1, 2, 3);
        assertVector(v, 1, 2, 3);
    }

    @Test
    public void testStaticAdd() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d v2 = new Vector3d(4, 5, 6);

        Vector3d result = Vector3d.add(v1, v2);

        assertVector(result, 5, 7, 9);
    }

    @Test
    public void testStaticSub() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d v2 = new Vector3d(4, 5, 6);

        Vector3d result = Vector3d.sub(v2, v1);

        assertVector(result, 3, 3, 3);
    }

    @Test
    public void testGetRelVector() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d v2 = new Vector3d(4, 5, 6);

        Vector3d result = Vector3d.getRelVector(v1, v2);

        assertVector(result, 3, 3, 3);
    }

    @Test
    public void testGetBase() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d result = Vector3d.getBase(v1);

        assertVector(result, 1, 2, 3);


        Vector3d v2 = new Vector3d(6, 2, 24);
        result = Vector3d.getBase(v2);

        assertVector(result, 3, 1, 12);


        Vector3d v3 = new Vector3d(9, 3, 36);
        result = Vector3d.getBase(v2);

        assertVector(result, 3, 1, 12);

    }

    @Test
    public void testAddVector() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d v2 = new Vector3d(4, 5, 6);

        Vector3d result = v1.add(v2);

        assertVector(result, 5, 7, 9);
    }

    @Test
    public void testAddInts() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);

        Vector3d result = v1.add(4, 5, 6);

        assertVector(result, 5, 7, 9);
    }

    @Test
    public void testSubVector() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);
        Vector3d v2 = new Vector3d(4, 5, 6);

        Vector3d result = v2.sub(v1);

        assertVector(result, 3, 3, 3);
    }

    @Test
    public void testSubInts() throws Exception {
        Vector3d v1 = new Vector3d(1, 2, 3);

        Vector3d result = v1.sub(-2, -1, 0);

        assertVector(result, 3, 3, 3);

    }

    private void assertVector(Vector3d v, int x, int y, int z) {
        assert v.x == x : "x Component wrong!";
        assert v.y == y : "y Component wrong!";
        assert v.z == z : "z Component wrong!";
    }
}