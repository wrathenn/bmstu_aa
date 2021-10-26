import algs.MatrixClassicMultiplier;
import algs.MatrixMultiplier;
import algs.MatrixVinogradMultiplier;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        MatrixMultiplier alg = new MatrixClassicMultiplier();
        MatrixMultiplier al1 = new MatrixVinogradMultiplier();

        int[][] m1 = new int[][]{{1, 2, 3}, {3, 2, 1}};
        int[][] m2 = new int[][]{{1, 2}, {2, 3}, {3, 1}};

        int[][] a = alg.multiply(m1, m2);
        int[][] b = al1.multiply(m1, m2);


        System.out.println(Arrays.deepToString(a));
        System.out.println(Arrays.deepToString(b));


    }
}
