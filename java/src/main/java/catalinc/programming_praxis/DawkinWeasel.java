package catalinc.programming_praxis;

import java.util.Random;

/**
 * Solution to http://programmingpraxis.com/2014/11/14/dawkins-weasel/
 */
public class DawkinWeasel {

    private static final Random RANDOM = new Random();

    private static final String ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

    private static int score(String s1, String s2) {
        int score = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(i)) score++;
        }
        return score;
    }

    private static String mutate(String s, int p) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (RANDOM.nextInt(100) < p) {
                sb.append(randomChar());
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }

    private static char randomChar() {
        return ASCII_UPPERCASE.charAt(RANDOM.nextInt(ASCII_UPPERCASE.length()));
    }

    private static String randomString(int length) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(randomChar());
        }
        return sb.toString();
    }

    private static int evolveTo(String ref) {
        String s = randomString(ref.length()),
               bestMatch = s;
        int iterations = 0,
            bestScore = score(s, ref);
        while (true) {
            iterations++;
            for (int i = 0; i < 100; i++) {
                String mutatedCopy = mutate(s, 5);
                int score = score(mutatedCopy, ref);
                if (score == ref.length()) {
                    // Perfect match
                    return iterations;
                }
                if (score > bestScore) {
                    bestScore = score;
                    bestMatch = mutatedCopy;
                }
            }
            s = bestMatch;
        }
    }

    public static void main(String[] args) {
        String ref = "METHINKS IT IS LIKE A WEASEL";
        System.out.println("Evolved in " + evolveTo(ref) + " iterations");
    }
}
