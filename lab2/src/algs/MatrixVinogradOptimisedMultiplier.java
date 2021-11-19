package algs;

public class MatrixVinogradOptimisedMultiplier implements MatrixMultiplier {
    @Override
    public int[][] multiply(int[][] m1, int[][] m2) {
        if (m1 == null || m2 == null) {
            return null;
        }

        if (m1[0].length != m2.length) {
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
            for (int k = 0; k < cols1 - 1; k += 2) {
                rowFactor[i] -= m1[i][k] * m1[i][k + 1];
            }
        }

        for (int i = 0; i < cols2; i++) {
            for (int k = 0; k < rows2 - 1; k += 2) {
                colFactor[i] += m2[k][i] * m2[k + 1][i];
            }
        }

        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                int buffer = rowFactor[i] - colFactor[j];

                for (int k = 0; k < cols1 - 1; k += 2) {
                    buffer += (m1[i][k] + m2[k + 1][j]) *
                            (m1[i][k + 1] + m2[k][j]);
                }

                if (cols1 % 2 == 1) {
                    buffer += m1[i][cols1 - 1] * m2[cols1 - 1][j];
                }

                result[i][j] = buffer;
            }
        }

        return result;
    }
}
