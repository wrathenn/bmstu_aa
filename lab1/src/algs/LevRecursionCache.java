package algs;

import java.util.Arrays;
import java.util.Objects;

public class LevRecursionCache extends StringDistanceAlgorithm {
    int[][] cache;

    public LevRecursionCache(String a, String b) {
        super(a, b);
    }

    public int findDifference() {
        cache = new int[a.length() + 1][b.length() + 1];
        for (int[] a : cache) {
            Arrays.fill(a, -1);
        }

        return findDifference(a, a.length(), b, b.length());
    }

    private int findDifference(String a, int aLen, String b, int bLen) {
        if (cache[aLen][bLen] != - 1) {
            return cache[aLen][bLen];
        }
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

        int min = Math.min(substitution, Math.min(deletion, insertion));
        cache[aLen][bLen] = min;
        return min;
    }
}
