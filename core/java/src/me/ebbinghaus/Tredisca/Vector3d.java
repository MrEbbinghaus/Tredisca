package me.ebbinghaus.Tredisca;

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
        return new Vector3d(a.x + b.x, a.y + b.y, a.z + b.z);
    }

    public static Vector3d sub(Vector3d a, Vector3d b) {
        return new Vector3d(a.x - b.x, a.y - b.y, a.z - b.z);
    }

    public static Vector3d getRelVector(Vector3d a, Vector3d b) {
        return sub(b, a);
    }

    public static Vector3d getBase(Vector3d a) {
        int ggt = ggt(a.x, ggt(a.y, a.z));
        return new Vector3d(a.x / ggt, a.y / ggt, a.z / ggt);
    }

    private static int ggt(int a, int b) {
        while (b != 0) {
            if (a > b) {
                a = a - b;
            } else {
                b = b - a;
            }
        }
        return a;
    }

    public Vector3d add(Vector3d vec) {
        return new Vector3d(x + vec.x, y + vec.y, z + vec.z);
    }

    public Vector3d add(int x, int y, int z) {
        return add(new Vector3d(x, y, z));
    }

    public Vector3d sub(Vector3d vec) {
        return sub(vec.x, vec.y, vec.z);
    }

    public Vector3d sub(int x, int y, int z) {
        return add(-x, -y, -z);
    }

}
