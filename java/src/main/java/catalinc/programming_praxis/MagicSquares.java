package catalinc.programming_praxis;

import java.util.Arrays;

/**
 * Solution to http://programmingpraxis.com/2014/12/12/magic-squares/
 */
public class MagicSquares {

    public static int[][] build(int n, String rule) {
        int r;
        int c;
        String[] ruleParts = rule.split(",");
        switch (ruleParts[0]) {
            case "bottom":
                r = n - 1;
                c = n / 2;
                break;
            case "top":
                r = 0;
                c = n / 2;
                break;
            case "left":
                r = n / 2;
                c = 0;
                break;
            case "right":
                r = n / 2;
                c = n - 1;
                break;
            default:
                throw new IllegalArgumentException("start position " + ruleParts[0] + " is invalid");
        }
        int[][] square = array(n, 0);
        square[r][c] = 1;
        for (int i = 2; i <= n * n; i++) {
            int oldR = r;
            int oldC = c;
            switch (ruleParts[1]) {
                case "down":
                    r = (r + 1) % n;
                    break;
                case "up":
                    r = (r - 1) % n;
                    if (r < 0) r = n - 1;
                    break;
                case "left":
                    c = (c - 1) % n;
                    if (c < 0) c = n - 1;
                    break;
                case "right":
                    c = (c + 1) % n;
                    break;
            }
            switch (ruleParts[2]) {
                case "down":
                    r = (r + 1) % n;
                    break;
                case "up":
                    r = (r - 1) % n;
                    if (r < 0) r = n - 1;
                    break;
                case "left":
                    c = (c - 1) % n;
                    if (c < 0) c = n - 1;
                    break;
                case "right":
                    c = (c + 1) % n;
                    break;
            }
            if (square[r][c] != 0) {
                switch (ruleParts[3]) {
                    case "down":
                        oldR = (oldR + 1) % n;
                        break;
                    case "up":
                        oldR = (oldR - 1) % n;
                        if (oldR < 0) oldR = n - 1;
                        break;
                    case "left":
                        oldC = (oldC - 1) % n;
                        if (oldC < 0) oldC = n - 1;
                        break;
                    case "right":
                        oldC = (oldC + 1) % n;
                        break;
                }
                square[oldR][oldC] = i;
                r = oldR;
                c = oldC;
            } else {
                square[r][c] = i;
            }
        }
        return square;
    }

    private static int[][] array(int size, int init) {
        int[][] a = new int[size][size];
        for (int r = 0; r < size; r++) {
            Arrays.fill(a[r], init);
        }
        return a;
    }

    public static void print(int[][] square) {
        StringBuilder output = new StringBuilder();
        for (int r = 0; r < square.length; r++) {
            for (int c = 0; c < square[r].length; c++) {
                if (c > 0) {
                    output.append(' ');
                }
                output.append(square[r][c]);
            }
            if (r < square.length - 1) {
                output.append('\n');
            }
        }
        System.out.println(output);
    }

    public static void main(String[] args) {
        print(build(3, "bottom,down,right,up"));
        print(build(13, "top,up,left,down"));
    }
}
