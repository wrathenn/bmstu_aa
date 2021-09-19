import algs.*;

import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;

public class StringDistanceAlgorithmsTester {
    private final String test1;
    private final String test2;
    private final int repeatTimes;
    private final int repeatRecursionTimes;

    public StringDistanceAlgorithmsTester(String a, String b, int repeatTimes, int repeatRecursionTimes) {
        test1 = a;
        test2 = b;
        this.repeatTimes = repeatTimes;
        this.repeatRecursionTimes = repeatRecursionTimes;
    }

    public static void testAlg(StringDistanceAlgorithm alg, String text, int repeatTimes) {
        System.out.println(text);

        for (int i = 0; i < repeatTimes; i++) {
            alg.findDifference();
        }

        ThreadMXBean threadMXBean = ManagementFactory.getThreadMXBean();
        long[] allThreadIds = threadMXBean.getAllThreadIds();
//        System.out.println("\tTotal JVM Thread count: " + allThreadIds.length);

        long nano = 0;
        for (long id : allThreadIds) {
            nano += threadMXBean.getThreadCpuTime(id);
        }
        System.out.printf("\tCPU time: %s ns\n", nano / repeatTimes);
    }

    public void testAllAlgs() {
        testAlg(new LevCasualMatrix(test1, test2), "Алгоритм Левенштейна (Итерационный)", repeatTimes);
        if (repeatRecursionTimes > 0) {
            testAlg(new LevRecursion(test1, test2), "Алгоритм Левенштейна (Рекурсивный)", repeatRecursionTimes);
        }
        testAlg(new LevRecursionCache(test1, test2), "Алгоритм Левенштейна (Рекурсивный с кэшем)", repeatTimes);


        testAlg(new LevDamCasualMatrix(test1, test2), "Алгоритм Дамерау-Левенштейна (Итерационный)", repeatTimes);
        if (repeatRecursionTimes > 0) {
            testAlg(new LevDamRecursion(test1, test2), "Алгоритм Дамерау-Левенштейна (Рекурсивный)", repeatRecursionTimes);
        }
        testAlg(new LevDamRecursionCache(test1, test2), "Алгоритм Дамерау-Левенштейна (Рекурсивный с кэшем)", repeatTimes);
    }
}
