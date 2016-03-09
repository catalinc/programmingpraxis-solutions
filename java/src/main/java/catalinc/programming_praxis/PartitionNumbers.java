package catalinc.programming_praxis;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.Map;

import static java.math.BigDecimal.ONE;
import static java.math.BigDecimal.ZERO;

public class PartitionNumbers {

    private static Map<BigDecimal, BigDecimal> cache =
            new HashMap<BigDecimal, BigDecimal>();

    private static final BigDecimal MINUS_ONE = new BigDecimal(-1);
    private static final BigDecimal TWO = new BigDecimal(2);
    private static final BigDecimal THREE = new BigDecimal(3);

    private static BigDecimal powMinus1(BigDecimal e) {
        if (e.remainder(TWO).equals(ZERO)) {
            return ONE;
        }
        return MINUS_ONE;
    }

    public static BigDecimal partitions(BigDecimal n) {
        if (n.equals(ZERO)) {
            return ONE;
        } else if (n.signum() < 0) {
            return ZERO;
        } else {
            if (cache.containsKey(n)) {
                return cache.get(n);
            } else {
                BigDecimal sum = ZERO;
                BigDecimal k = ONE;
                while (k.compareTo(n) <= 0) {
                    sum = sum.add(powMinus1(k.add(ONE)).multiply(
                            partitions(n.subtract((k.multiply(k.multiply(THREE).subtract(ONE))).divide(TWO)))
                                    .add(
                                            partitions(n.subtract((k.multiply(k.multiply(THREE).add(ONE)).divide(TWO)))))));
                    k = k.add(ONE);
                }
                cache.put(n, sum);
                return sum;
            }
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java catalinc.programming_praxis.PartitionNumbers NUMBER");
            System.exit(1);
        }
        BigDecimal n = new BigDecimal(args[0]);
        long start = System.currentTimeMillis();
        System.out.println("partitions(" + n + ")=" + partitions(n));
        long end = System.currentTimeMillis();
        System.out.println((end - start) + " msec");
    }
}
