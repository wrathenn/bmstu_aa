package algs;

public class MatrixClassicMultiplier implements MatrixMultiplier {
    @Override
    public int[][] multiply(int[][] m1, int[][] m2) {
        if (m1 == null || m2 == null) {
            return null;
        }

        if (m1.length != m2[0].length) {
            return null;
        }

        int rows1 = m1.length;
        int rows2 = m2.length;
        int cols1 = m1[0].length;
        int cols2 = m2[0].length;

        int[][] result = new int[rows1][cols2];

        for (int i = 0; i < rows1; i++) {
            for (int k = 0; k < cols2; k++) {
                for (int m = 0; m < cols1; m++) {
                    result[i][k] += m1[i][m] * m2[m][k];
                }
            }
        }

        return result;
    }
}
