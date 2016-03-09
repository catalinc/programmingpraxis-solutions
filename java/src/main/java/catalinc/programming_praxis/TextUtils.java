package catalinc.programming_praxis;

public class TextUtils {

    public static String entab(final String text, final int tabSize) {
        final StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            final char c = text.charAt(i);
            if (c != ' ') {
                result.append(text.substring(i));
                break;
            }
            if ((i + 1) % tabSize == 0) {
                result.append('\t');
            }
        }
        return result.toString();
    }

    public static String detab(final String text, final int tabSize) {
        final String spaces = replicate(' ', tabSize);
        final StringBuilder result = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            final char c = text.charAt(i);
            if (c != '\t') {
                result.append(text.substring(i));
                break;
            }
            result.append(spaces);
        }
        return result.toString();
    }

    private static String replicate(final char c, final int count) {
        final StringBuilder result = new StringBuilder();
        for (int i = 0; i < count; i++) {
            result.append(c);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        final String text = "  text";
        final int tabSize = 2;
        System.out.printf("%-15s:|%s|\n", "original", text);
        System.out.printf("%-15s:|%s|\n", "spaces -> tabs",
                entab(text, tabSize));
        System.out.printf("%-15s:|%s|\n", "tabs -> spaces",
                detab(entab(text, tabSize), tabSize));
    }
}
