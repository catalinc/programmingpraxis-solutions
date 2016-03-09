package catalinc.programming_praxis;

/**
 * Matcher for simple regular expressions.
 */
public class Matcher {

    public static boolean match(String regexp, String text) {
        if (regexp.charAt(0) == '^') {
            return matchhere(regexp, 1, text, 0);
        }
        int i = 0;
        while (i < text.length()) {
            if (matchhere(regexp, 0, text, i)) {
                return true;
            }
            i++;
        }
        return false;
    }

    private static boolean matchhere(String regexp, int i, String text, int j) {
        if (i == regexp.length()) {
            return true;
        }
        if (regexp.charAt(i + 1) == '*') {
            return matchstar(regexp.charAt(i), regexp, i + 2, text, j);
        }
        if (regexp.charAt(i) == '$' && i == regexp.length() - 1) {
            return j == text.length();
        }
        if (j < text.length() && (regexp.charAt(i) == '.' || regexp.charAt(i) == text.charAt(j))) {
            return matchhere(regexp, i + 1, text, j + 1);
        }
        return false;
    }

    private static boolean matchstar(char c, String regexp, int i, String text, int j) {
        while (j < text.length() && (text.charAt(j) == c || text.charAt(j) == '.')) {
            if (matchhere(regexp, i, text, j)) {
                return true;
            }
            j++;
        }
        return false;
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java catalinc.programming_praxis.Matcher regexp text");
            System.exit(1);
        }
        System.out.println(args[0]
                + (Matcher.match(args[0], args[1]) ? " " : " does not ")
                + "match " + args[1]);
    }
}
