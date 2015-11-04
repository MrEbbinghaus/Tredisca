package Tredisca;

/**
 * Created by bjebb on 04.11.15.
 */
public class Vector3d {
    public int x, y, z;

    public Vector3d(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public static Vector3d add(Vector3d a, Vector3d b) {
        return new Vector3d(a.x + b.x, a.y + b.y, a.z + b.y);
    }

    public static Vector3d sub(Vector3d a, Vector3d b) {
        return new Vector3d(a.x - b.x, a.y - b.y, a.z - b.z);
    }

    public static Vector3d getRelVector(Vector3d a, Vector3d b) {
        return sub(b, a);
    }

    public static Vector3d getBase(Vector3d a) {
        return new Vector3d(a.x > 0 ? 1 : a.x < 0 ? -1 : 0,
                a.y > 0 ? 1 : a.y < 0 ? -1 : 0,
                a.z > 0 ? 1 : a.z < 0 ? -1 : 0
        );
    }

    public void add(Vector3d vec) {
        this.x += vec.x;
        this.y += vec.y;
        this.z += vec.z;
    }

    public void add(int x, int y, int z) {
        add(new Vector3d(x, y, z));
    }

    public void sub(Vector3d vec) {
        sub(vec.x, vec.y, vec.z);
    }

    public void sub(int x, int y, int z) {
        add(-x, -y, -z);
    }

}
