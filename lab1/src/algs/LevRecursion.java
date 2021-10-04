package algs;

import java.util.Objects;

public class LevRecursion extends StringDistanceAlgorithm {
    public LevRecursion(String a, String b) {
        super(a, b);
    }

    public int findDifference() {
        return findDifference(a, a.length(), b, b.length());
    }

    private int findDifference(String a, int aLen, String b, int bLen) {
        if (aLen == 0) {
            return bLen;
        }
        if (bLen == 0) {
            return aLen;
        }

        int deletion = findDifference(a, aLen - 1, b, bLen) + 1;
        int insertion = findDifference(a, aLen, b, bLen - 1) + 1;

        int match = Objects.equals(a.charAt(aLen - 1), b.charAt(bLen - 1)) ? 0 : 1;
        int substitution = findDifference(a, aLen - 1, b, bLen - 1) + match;

        return Math.min(substitution, Math.min(deletion, insertion));
    }
}
