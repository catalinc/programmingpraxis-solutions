package catalinc.programming_praxis.sum;

import static java.lang.Math.floor;
import static java.lang.Math.round;
import static java.lang.Math.sqrt;

import java.util.LinkedList;
import java.util.List;

/**
 * Write a function that, given a number n, finds all pairs of numbers x and y,
 * with x ? y ? 0, such that x� + y� = n; for instance, 50 = 7� + 1� = 5� + 5�,
 * 48612265 = 6972� + 59� = 6971� + 132� = �, and 999 has no solutions.
 */
public class SumOfTwoSquares {

    public static List<List<Long>> solve(long n) {
        List<List<Long>> solutions = new LinkedList<List<Long>>();
        long x = round(floor(sqrt(n))), y = 0;
        do {
            long val = x * x + y * y;
            if (val == n) {
                List<Long> solution = new LinkedList<Long>();
                solution.add(x);
                solution.add(y);
                solutions.add(solution);
                x--;
                y++;
            } else if (val > n) {
                x--;
            } else {
                y++;
            }
        } while (x >= y);
        return solutions;
    }


}
