package catalinc.programming_praxis;

import java.util.Arrays;

/**
 * Solution to http://programmingpraxis.com/2014/11/21/an-array-of-zeroes/
 */
public class ArrayOfZeroes {

    public static int compactZeroes(int[] a) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 0) {
                boolean swapped = false;
                for (int j = a.length - 1; j > i; j--) {
                    if (a[j] != 0) {
                        swap(a, i, j);
                        swapped = true;
                        break;
                    }
                }
                if (!swapped) break;
            }
        }
        for (int i = 0; i < a.length; i++) {
            if (a[i] == 0) return i;
        }
        return -1;
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    public static void main(String[] args) {
        int[] a = {1, 0, 2, 0, 0, 3, 4};
        int n = compactZeroes(a);
        System.out.println(Arrays.toString(a) + " " + n);
    }
}
