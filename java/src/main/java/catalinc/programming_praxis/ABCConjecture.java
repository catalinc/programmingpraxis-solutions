package main.java.catalinc.programming_praxis;

import java.util.*;

/**
 * A solution to http://programmingpraxis.com/2012/09/18/abc-conjecture/
 */
public class ABCConjecture {

    public static void main(String[] args) {
        List<ABCTriple> triples = abc(1000);
        Collections.sort(triples, new Comparator<ABCTriple>() {
            public int compare(ABCTriple t1, ABCTriple t2) {
                if (t1.q < t2.q) return 1;
                return -1;
            }
        });
        for (ABCTriple t : triples) {
            System.out.println(t);
        }
    }

    public static List<ABCTriple> abc(final int n) {
        List<ABCTriple> result = new LinkedList<ABCTriple>();
        for (int a = 1; a <= n - 1; a++) {
            for (int b = a + 1; b <= n; b++) {
                int c = a + b;
                if (c < n && coPrime(a, b, c)) {
                    double q = q(a, b, c);
                    if (q > 1.0) {
                        result.add(new ABCTriple(a, b, c, q));
                    }
                }
            }
        }
        return result;
    }

    public static double q(int a, int b, int c) {
        return Math.log(c) / Math.log(rad(a * b * c));
    }

    public static int rad(int n) {
        return product(unique(primeFactors(n)));
    }

    private static boolean coPrime(Integer... numbers) {
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (gcd(numbers[i], numbers[j]) != 1) return false;
            }
        }
        return true;
    }

    private static int gcd(int a, int b) {
        int max = Math.max(a, b);
        int min = Math.min(a, b);
        while (min != 0) {
            int r = max % min;
            max = min;
            min = r;
        }
        return max;
    }

    private static int product(Collection<Integer> numbers) {
        int result = 1;
        for (int i : numbers) {
            result *= i;
        }
        return result;
    }

    private static Set<Integer> unique(Collection<Integer> numbers) {
        return new HashSet<Integer>(numbers);
    }

    private static List<Integer> primeFactors(int n) {
        List<Integer> primeFactors = new LinkedList<Integer>();
        for (int p : PRIMES) {
            if (p * p > n) break;
            while (n % p == 0) {
                primeFactors.add(p);
                n /= p;
            }
        }
        if (n > 1) primeFactors.add(n);
        return primeFactors;
    }

    private static List<Integer> PRIMES = sieve(1000);

    private static List<Integer> sieve(int n) {
        List<Integer> primes = new LinkedList<Integer>();
        BitSet sieve = new BitSet(n + 1);
        for (int i = 2; i * i <= n; i = sieve.nextClearBit(i + 1)) {
            primes.add(i);
            for (int j = i + i; j <= n; j += i) {
                sieve.set(j);
            }
        }
        return primes;
    }

}

class ABCTriple {
    final int a;
    final int b;
    final int c;
    final double q;

    ABCTriple(int a, int b, int c, double q) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.q = q;
    }

    public String toString() {
        return q + " [" + a + ", " + b + ", " + c + "]";
    }
}