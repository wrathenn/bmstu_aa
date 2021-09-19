package algs;

public abstract class StringDistanceAlgorithm {
    protected String a;
    protected String b;

    public StringDistanceAlgorithm(String a, String b) {
        this.a = a;
        this.b = b;
    }

    abstract public int findDifference();
}
