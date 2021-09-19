package algs;

import java.util.Objects;

public class LevDamCasualMatrix extends StringDistanceAlgorithm {
    private int[][] matrix;

    public LevDamCasualMatrix(String a, String b) {
        super(a, b);
        matrix = new int[a.length() + 1][b.length() + 1];
    }

    public int findDifference() {

        for (int col = 0; col < matrix[0].length; col++) {
            matrix[0][col] = col;
        }

        for (int row = 1; row < matrix.length; row++) {
            matrix[row][0] = row;
        }

        for (int row = 1; row < matrix.length; row++) {
            for (int col = 1; col < matrix[0].length; col++) {
                int valueFromTheRight = matrix[row][col - 1] + 1;
                int valueFromTheUp = matrix[row - 1][col] + 1;

                int match = Objects.equals(a.charAt(row - 1), b.charAt(col - 1)) ? 0 : 1;
                int valueFromDiagonal = matrix[row - 1][col - 1] + match;

                matrix[row][col] = Math.min(valueFromTheRight, Math.min(valueFromTheUp, valueFromDiagonal));

                int swap = Integer.MAX_VALUE;
                if (row > 1 && col > 1) {
                    if (Objects.equals(a.charAt(row - 1), b.charAt(col - 2)) &&
                            Objects.equals(a.charAt(row - 2), b.charAt(col - 1))) {
                        swap = matrix[row - 2][col - 2] + 1;
                    }
                }

                matrix[row][col] = Math.min(Math.min(valueFromTheRight, valueFromTheUp),
                        Math.min(swap, valueFromDiagonal));
            }
        }

        return matrix[a.length()][b.length()];
    }
}
