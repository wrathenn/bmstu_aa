package algs;

public class MatrixVinogradMultiplier implements MatrixMultiplier {
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

        int[] rowFactor = new int[rows1];
        int[] colFactor = new int[cols2];

        for (int i = 0; i < rows1; i++) {
            for (int k = 0; k < cols1 / 2; k++) {
                rowFactor[i] = rowFactor[i] + m1[i][2 * k] * m1[i][2 * k + 1];
            }
        }

        for (int i = 0; i < cols2; i++) {
            for (int k = 0; k < rows2 / 2; k++) {
                colFactor[i] = colFactor[i] + m2[2 * k][i] * m2[2 * k + 1][i];
            }
        }

        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                result[i][j] = -rowFactor[i] - colFactor[j];
                for (int k = 0; k < cols1 / 2; k++) {
                    result[i][j] = result[i][j] + (m1[i][2 * k] + m2[2 * k + 1][j]) *
                            (m1[i][2 * k + 1] + m2[2 * k][j]);
                }
            }
        }

        if (cols1 % 2 == 1) {
            for (int i = 0; i < rows1; i++) {
                for (int k = 0; k < cols2; k++) {
                    result[i][k] = result[i][k] + m1[i][cols1 - 1] * m2[cols1 - 1][k];
                }
            }
        }

        return result;
    }
}
