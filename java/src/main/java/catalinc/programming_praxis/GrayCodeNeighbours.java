package catalinc.programming_praxis;

/**
 * Solution to http://programmingpraxis.com/2014/12/02/gray-code-neighbors/
 */
public class GrayCodeNeighbours {

    private static boolean consecutiveGrayCodes(int a, int b) {
        int x = a ^ b;
        return x % 2 == 0 && (x == (x & -x));
    }

    public static void main(String[] args) {
        int[][] testData = {{3, 2}, {6, 7}, {5, 4}, {88, 72}, {88, 90}, {3, 4},  {88, 91}};
        for (int[] pair : testData) {
            int a = pair[0];
            int b = pair[1];
            System.out.println(a + " " + b + " -> " + consecutiveGrayCodes(a, b));
        }
    }
}
