import algs.MatrixMultiplier;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;
import java.util.Arrays;

public class MatrixAlgTester {
    private final MatrixMultiplier algorithm;
    private final int[][] m1;
    private final int[][] m2;
    private final int repeats;

    public MatrixAlgTester(MatrixMultiplier algorithm, int[][] m1, int[][] m2, int repeats) {
        this.algorithm = algorithm;
        this.m1 = m1;
        this.m2 = m2;
        this.repeats = repeats;
    }

    public void test(String name) {
        System.out.println("______________________");
        System.out.println(name);

        for (int i = 0; i < repeats; i++) {
            algorithm.multiply(m1, m2);
        }

        ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
        long[] allThreadIds = threadMXBean.getAllThreadIds();

        long nano = 0;
        for (long id : allThreadIds) {
            nano += threadMXBean.getThreadCpuTime(id);
        }

        nano /= repeats;
        if (repeats != 1) {
            System.out.println("\tCPU time: " + nano);
        }
        System.out.println("\tОтвет: " + Arrays.deepToString(algorithm.multiply(m1, m2)));
    }
}
