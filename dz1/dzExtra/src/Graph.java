import java.util.Arrays;

public class Graph {
    private final int[][] connections;

    public Graph(int[][] connections) {
        this.connections = connections;
    }

    public Graph(int size) {
        this.connections = new int[size][size];
    }

    public void setConnection(int i, int j, int weight) {
        connections[i][j] = weight;
        connections[j][i] = weight;
    }

    public int getConnection(int i, int j) {
        return connections[i][j];
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder("Graph:\n");
        for (int[] connection : connections) {
            result.append(Arrays.toString(connection)).append("\n");
        }

        return result.toString();
    }

    public Graph primeAlg() {
        int size = connections.length;
        Graph ostov = new Graph(size);

        boolean[] selected = new boolean[size];
        selected[0] = true;

        int currentNode = 0;

        while (currentNode < size - 1) {
            int minWeight = Integer.MAX_VALUE;
            int x = 0;
            int y = 0;

            for (int i = 0; i < size; i++) {
                if (selected[i]) {
                    for (int k = 0; k < size; k++) {
                        if (!selected[k] && connections[i][k] != 0) {
                            if (minWeight > connections[i][k]) {
                                minWeight = connections[i][k];
                                x = i;
                                y = k;
                            }
                        }
                    }
                }
            }

            ostov.setConnection(x, y, minWeight);
            selected[y] = true;
            currentNode++;
        }

        return ostov;
    }
}
