package catalinc.programming_praxis;

import java.util.ArrayList;
import java.util.List;

/**
 * Solution to http://programmingpraxis.com/2014/11/18/damms-algorithm/
 */
public class DammAlgorithm {

    private static final int[][] CHECK_DIGIT_TABLE = {
            {0, 3, 1, 7, 5, 9, 8, 6, 4, 2},
            {7, 0, 9, 2, 1, 5, 4, 8, 6, 3},
            {4, 2, 0, 6, 8, 7, 1, 3, 5, 9},
            {1, 7, 5, 0, 9, 8, 3, 4, 2, 6},
            {6, 1, 2, 3, 0, 4, 5, 9, 7, 8},
            {3, 6, 7, 4, 2, 0, 9, 5, 8, 1},
            {5, 8, 6, 9, 7, 2, 0, 1, 3, 4},
            {8, 9, 4, 5, 3, 6, 2, 0, 1, 7},
            {9, 4, 3, 8, 6, 1, 7, 2, 0, 9},
            {2, 5, 8, 1, 4, 3, 6, 7, 9, 0}
    };

    public static int addCheckDigit(int n) {
        int checkDigit = 0;
        for (Integer digit : digits(n)) {
            checkDigit = CHECK_DIGIT_TABLE[checkDigit][digit];
        }
        return n * 10 + checkDigit;
    }

    private static List<Integer> digits(int n) {
        List<Integer> digits = new ArrayList<>();
        int d;
        while (n > 0) {
            d = n % 10;
            n = (n - d) / 10;
            digits.add(0, d);
        }
        return digits;
    }

    public static boolean hasValidCheckDigit(int n) {
        int checkDigit = 0;
        for (Integer digit : digits(n)) {
            checkDigit = CHECK_DIGIT_TABLE[checkDigit][digit];
        }
        return checkDigit == 0;
    }

    public static void main(String[] args) {
        System.out.println(addCheckDigit(572));
        System.out.println(hasValidCheckDigit(5724));
    }
}
