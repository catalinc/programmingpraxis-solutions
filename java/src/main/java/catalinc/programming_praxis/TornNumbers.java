package main.java.catalinc.programming_praxis;

/**
 * Solution to http://programmingpraxis.com/2014/09/16/torn-numbers/
 */
public final class TornNumbers {

    public static boolean isTorn(int n) {
        if (n < 10) return false;
        String s = String.valueOf(n);
        for (int i = 1; i < s.length() - 1; i++) {
            int p1 = Integer.parseInt(s.substring(0, i));
            int p2 = Integer.parseInt(s.substring(i));
            int sum = p1 + p2;
            if (sum * sum == n) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(isTorn(88209));
        System.out.println(isTorn(123));
    }
}
