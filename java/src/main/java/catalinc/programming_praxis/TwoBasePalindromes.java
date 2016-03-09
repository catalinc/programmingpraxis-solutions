package main.java.catalinc.programming_praxis;

/**
 * Solution to http://programmingpraxis.com/2014/10/21/two-base-palindromes/
 */
public class TwoBasePalindromes {

    private static final class LongWrapper {
        private final String dec;
        private final String oct;

        private LongWrapper(long value) {
            this.dec = Long.toString(value);
            this.oct = Long.toOctalString(value);
        }

        private boolean isDecAndOctPalindrome() {
            return isPalindrome(this.dec) && isPalindrome(this.oct);
        }

        private boolean isPalindrome(String s) {
            int i = 0;
            int j = s.length() - 1;
            while (i < j) {
                if (s.charAt(i) != s.charAt(j)) return false;
                i++;
                j--;
            }
            return true;
        }

        @Override
        public String toString() {
            return "LongWrapper{" +
                    "dec='" + dec + '\'' +
                    ", oct='" + oct + '\'' +
                    '}';
        }
    }

    public static void main(String[] args) {
        for (long n = 0; n < Long.MAX_VALUE; n++) {
            LongWrapper lw = new LongWrapper(n);
            if (lw.isDecAndOctPalindrome()) {
                System.out.println(n);
            }
        }
    }
}
