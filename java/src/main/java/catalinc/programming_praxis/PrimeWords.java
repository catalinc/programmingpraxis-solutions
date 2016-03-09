package catalinc.programming_praxis;

public class PrimeWords {

    public static boolean isPrime(String base36Num) {
        return isPrime(Long.parseLong(base36Num, 36));
    }

    private static boolean isPrime(long n) {
        final long sqrt = Math.round(Math.sqrt(n));
        for (long i = 2; i <= sqrt; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java catalinc.programming_praxis.PrimeWords BASE36NUM");
            System.exit(1);
        }
        final String base36Num = args[0];
        System.out.println(base36Num + " is "
                + (isPrime(base36Num) ? "prime" : "composite"));
    }
}
