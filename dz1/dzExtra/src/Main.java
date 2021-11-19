public class Main {
    public static void main(String[] args) {
        int size = 5;
        int[][] connections = new int[][]{
                {0, 9, 75, 0, 0},
                {9, 0, 95, 19, 42},
                {75, 95, 0, 51, 66},
                {0, 19, 51, 0, 31},
                {0, 42, 66, 31, 0}
        };

        Graph graph = new Graph(connections);

        Graph ostov = graph.primeAlg();

        System.out.println(graph);
        System.out.println(ostov);
    }
}
