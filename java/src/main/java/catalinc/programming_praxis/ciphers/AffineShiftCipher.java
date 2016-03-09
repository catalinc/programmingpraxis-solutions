package catalinc.programming_praxis.ciphers;

import java.util.HashMap;
import java.util.Map;

import static java.lang.Math.floor;

/**
 * Simple but cryptographically weak. It works by mapping the twenty-six letters of the alphabet
 * onto the integers 0 through 25, then applying the function (ax + b) mod 26 to each character in turn,
 * finally mapping back from integers to letters. The key is formed by the numbers a and b.
 * Decryption is the inverse operation, a^-1(x ? b) mod 26, where a^-1 is the modular inverse of a modulo m;
 * this means that a and m must be coPrime.
 * For instance, the plain-text PROGRAMMINGPRAXIS is enciphered with a=5 and b=8 as FPAMPIQQWVMFPITWU,
 * and deciphered with 21 as the modular inverse.
 */
public class AffineShiftCipher {
    private static String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    private static Map<Character, Integer> CHARACTER_TO_ORDINAL;

    static {
        CHARACTER_TO_ORDINAL = new HashMap<Character, Integer>();
        for (int i = 0; i < ALPHABET.length(); i++) {
            CHARACTER_TO_ORDINAL.put(ALPHABET.charAt(i), i);
        }
    }

    private Key key;
    private int inverseMod;

    /**
     * Representation of cipher key.
     */
    public static class Key {
        private int a;
        private int b;

        public Key(int a, int b) {
            this.a = a;
            this.b = b;
        }

        public int getA() {
            return a;
        }

        public int getB() {
            return b;
        }

        @Override
        public String toString() {
            return "Key{" +
                    "a=" + a +
                    ", b=" + b +
                    '}';
        }
    }

    /**
     * @param key Cipher key.
     */
    public AffineShiftCipher(Key key) {
        validateKey(key);
        this.key = key;
        this.inverseMod = inverseMod(key.getA(), ALPHABET.length());
    }

    /**
     * Encrypt message.
     *
     * @param text message to be encrypted
     * @return encrypted message
     */
    public String encrypt(String text) {
        return transformText(text, new OrdinalMappingFunction() {
            public int map(int ord) {
                return mod(key.getA() * ord + key.getB(), ALPHABET.length());
            }
        });
    }

    /**
     * Decrypt message.
     *
     * @param text message to be decrypted
     * @return decrypted message
     */
    public String decrypt(String text) {
        return transformText(text, new OrdinalMappingFunction() {
            public int map(int ord) {
                return mod(inverseMod * (ord - key.getB()), ALPHABET.length());
            }
        });
    }

    private void validateKey(Key key) {
        if (key == null) {
            throw new IllegalArgumentException("key cannot be null");
        }
        if (!coPrime(key.getA(), ALPHABET.length())) {
            throw new IllegalArgumentException("key.getA() = " + key.getA() +
                    " and ALPHABET.length() = " + ALPHABET.length() + " must be coprime");
        }
    }

    private String transformText(String text, OrdinalMappingFunction function) {
        if (nullOrEmpty(text)) {
            return text;
        }
        String input = text.toUpperCase();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            Character ch = input.charAt(i);
            Integer ord = CHARACTER_TO_ORDINAL.get(ch);
            if (ord != null) {
                // char in alphabet, transform
                result.append(ALPHABET.charAt(function.map(ord)));
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }

    private interface OrdinalMappingFunction {
        public int map(int ord);
    }

    private boolean nullOrEmpty(String str) {
        return str == null || str.equals("");
    }

    private boolean coPrime(int a, int b) {
        return gcd(a, b) == 1;
    }

    private int gcd(int a, int b) {
        int tmp;
        while (b != 0) {
            tmp = b;
            b = mod(a, b);
            a = tmp;
        }
        return a;
    }

    private int inverseMod(int a, int m) {
        int mOrig = m;
        int im = 0;
        int lastIm = 1;
        int tmp;
        int q;

        while (m != 0) {
            q = a / m;
            // gcd
            tmp = m;
            m = mod(a, m);
            a = tmp;
            // inverse mod
            tmp = im;
            im = lastIm - q * im;
            lastIm = tmp;
        }   

        return mod(lastIm + mOrig, mOrig);
    }

    private int mod(int a, int b) {
        return (int) (a - floor((double) a / b) * b);
    }
}
