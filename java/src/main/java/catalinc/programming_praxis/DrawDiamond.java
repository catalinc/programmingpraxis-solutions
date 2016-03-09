package catalinc.programming_praxis;

import java.util.Arrays;

public class DrawDiamond {

    public static void draw(int size, boolean filled) {
        int middle = (2 * size - 1) / 2;
        char[] line = new char[2 * size - 1];
        for (int i = 0; i <= middle; i++) {
            Arrays.fill(line, ' ');
            int l = middle - i;
            int r = middle + i;
            line[l] = '*';
            line[r] = '*';
            if (filled) {
                for (int j = l + 2; j < r; j += 2) {
                    line[j] = '*';
                }
            }
            println(line);
        }
        for (int i = middle - 1; i >= 0; i--) {
            Arrays.fill(line, ' ');
            int l = middle - i;
            int r = middle + i;
            line[l] = '*';
            line[r] = '*';
            if (filled) {
                for (int j = l + 2; j < r; j += 2) {
                    line[j] = '*';
                }
            }
            println(line);
        }
    }

    private static void println(char[] chars) {
        StringBuilder out = new StringBuilder();
        out.append(chars);
        System.out.println(out);
    }

    public static void main(String[] args) {
        draw(5, true);
    }
}