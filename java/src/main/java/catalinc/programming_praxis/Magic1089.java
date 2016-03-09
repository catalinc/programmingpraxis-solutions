package catalinc.programming_praxis;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Magic1089 {

    private static List<Integer> digits(int n) {
        List<Integer> digits = new ArrayList<>(3);
        while (n > 0) {
            int d = n % 10;
            digits.add(0, d);
            n = (n - d) / 10;
        }
        return digits;
    }

    private static int toInt(List<Integer> digits) {
        if (digits.isEmpty()) {
            return 0;
        }
        int n = digits.get(digits.size() - 1);
        int p = 10;
        for (int i = digits.size() - 2; i >= 0; i--) {
            int d = digits.get(i);
            n += (d * p);
            p *= 10;
        }
        return n;
    }

    private static int reverse(int n) {
        List<Integer> digits = digits(n);
        Collections.reverse(digits);
        return toInt(digits);
    }

    public static int magic(int n) {
        int r = n - reverse(n);
        return r + reverse(r);
    }

    public static void main(String[] args) {
        System.out.println(magic(642));
    }
}
