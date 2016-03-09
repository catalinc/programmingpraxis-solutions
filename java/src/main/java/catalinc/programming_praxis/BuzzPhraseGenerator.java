package catalinc.programming_praxis;

import java.util.Random;

/**
 * Solution http://programmingpraxis.com/2014/11/25/thou-impertinent-urchin-faced-miscreant/
 */
public class BuzzPhraseGenerator {

    private static final Random RANDOM = new Random();

    private static final String[][] BUZZ_WORDS_TABLE = {
            {"integrated", "total", "systematized", "parallel", "functional", "responsive", "optional", "synchronized", "compatible", "balanced"},
            {"management", "organizational", "monitored", "reciprocal", "digital", "logistical", "transitional", "incremental", "third-generation", "policy"},
            {"options", "flexibility", "capability", "mobility", "programming", "concept", "time-phase", "projection", "hardware", "contingency"}
    };

    public static String buzzPhrase() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < BUZZ_WORDS_TABLE.length; i++) {
            String[] words = BUZZ_WORDS_TABLE[i];
            sb.append(words[RANDOM.nextInt(words.length)]);
            if (i != BUZZ_WORDS_TABLE.length - 1) {
                sb.append(' ');
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(buzzPhrase());
    }
}

