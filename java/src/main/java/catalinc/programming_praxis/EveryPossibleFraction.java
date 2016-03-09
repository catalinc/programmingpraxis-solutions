package catalinc.programming_praxis;

/**
 * Solution to http://programmingpraxis.com/2014/12/09/every-possible-fraction
 */
public class EveryPossibleFraction {

    private static class F {
        final int num;
        final int den;

        F(int num, int den) {
            this.num = num;
            this.den = den;
        }

        F n() {
            return new F((num / den) * den, den);
        }

        F y() {
            return new F(num - n().num, den);
        }

        F next() {
            return new F(den, n().num - y().num + den);
        }

        @Override
        public String toString() {
            return num + "/" + den;
        }
    }

    public static void main(String[] args) {
        F f = new F(1, 1);
        for (int i = 1; i <= 20; i++) {
            System.out.println(f);
            f = f.next();
        }
    }

}
