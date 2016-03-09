package catalinc.programming_praxis.piglatin;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class PigLatin {

    private static final Set<Character> vowels =
            new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

    static boolean isVowel(char c) {
        return vowels.contains(c);
    }

    public static String translate(final String word) {
        if (word == null || word.length() == 0) {
            return word;
        }
        if (isVowel(word.charAt(0))) {
            return word + "-way";
        }
        for (int i = 0; i < word.length(); i++) {
            if (isVowel(word.charAt(i))) {
                return word.substring(i)
                        + "-" + word.substring(0, i) + "ay";
            }
        }
        return "-" + word + "ay";
    }

    public static String untranslate(final String word) {
        if (word == null || word.length() == 0) {
            return word;
        }
        String prefix = null;
        String suffix = null;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == '-') {
                prefix = word.substring(0, i);
                suffix = word.substring(i + 1);
                break;
            }
        }
        if ("way".equals(suffix)) {
            return prefix;
        }
        return suffix.substring(0, suffix.length() - 2) + prefix;
    }
}
