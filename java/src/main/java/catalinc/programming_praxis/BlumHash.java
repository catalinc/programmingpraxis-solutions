package catalinc.programming_praxis;

import java.util.function.Function;

public class BlumHash {

    private Function<Character, Integer> f;
    private int[] g;

    public BlumHash(Function<Character, Integer> f, int[] g) {
        this.f = f;
        this.g = g;
    }

    public String hash(final String s) {
        int n = s.length();
        int[] d = new int[n];
        for (int i = 0; i < n; i++) {
            d[i] = f.apply(s.charAt(i));
        }
        int[] h = new int[n];
        h[0] = next((d[0] + d[n - 1]) % 10);
        for (int i = 1; i < n; i++) {
            h[i] = next((h[i - 1] + d[i]) % 10);
        }
        StringBuilder sb = new StringBuilder(n);
        for (int i = 0; i < n; i++) {
            sb.append(h[i]);
        }
        return sb.toString();
    }

    private int next(int n) {
        for (int i = 0; i < g.length; i++) {
            if (g[i] == n) {
                return g[(i+1) % g.length];
            }
        }
        throw new IllegalArgumentException(n + " not found");
    }

    public static void main(String[] args) {
        BlumHash hasher = new BlumHash(c -> {
            switch (c) {
                case 'a': return 8;
                case 'b': return 3;
                case 'c': return 7;
                default:
                    return c % 10;
            }
        }, new int[]{0,2,9,8,7,3,6,5,1,4});
        System.out.println(hasher.hash("abc"));
    }
}
