package catalinc.programming_praxis;

public class BlumBlumShubCipher {

    public static class RandomGen {
        private int v;
        private int n;

        public RandomGen(int s, int n) {
            this.v = s;
            this.n = n;
        }

        public int next() {
            v = (v * v) % n;
            return v % 256;
        }
    }

    public static String encrypt(final int s, final int n, final String text) {
        final StringBuilder encrypted = new StringBuilder();
        final RandomGen rnd = new RandomGen(s, n);
        for (char c : text.toCharArray()) {
            encrypted.append((char) (c ^ rnd.next()));
        }
        return encrypted.toString();
    }

    public static void main(String[] args) {
        final String text = "PROGRAMMING PRAXIS";
        final int s = 17;
        final int n = 974153;
        final String encrypted = encrypt(s, n, text);
        System.out.println(text + " -> " + encrypted);
        System.out.println(encrypted + " -> " + encrypt(s, n, encrypted));
    }
}

