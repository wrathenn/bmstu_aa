public class Main {
    public static void main(String[] args) {
        StringDistanceAlgorithmsTester tester;

        int repeat = 1000000;
        int repeatRecursion = 1000;

        // Тесты на правильность
        tester = new StringDistanceAlgorithmsTester("kot", "skat", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("solution", "slouiton", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("fumo", "mofu", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("", "", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("", "aoa", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("aoa", "", repeat, repeatRecursion);
        tester.testAllAlgs();
        tester = new StringDistanceAlgorithmsTester("текст", "ткскт", repeat, repeatRecursion);
        tester.testAllAlgs();
    }
}
