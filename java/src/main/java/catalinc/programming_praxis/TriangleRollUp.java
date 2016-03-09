package catalinc.programming_praxis;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class TriangleRollUp {

    public static List<List<Integer>> rollUp(Integer... ints) {
        List<List<Integer>> triangle = new LinkedList<>();
        triangle.add(0, Arrays.asList(ints));
        for (; ; ) {
            List<Integer> current = new LinkedList<>();
            List<Integer> previous = triangle.get(0);
            for (int i = 0; i < previous.size() - 1; i++) {
                current.add(previous.get(i) + previous.get(i + 1));
            }
            triangle.add(0, current);
            if (current.size() == 1) {
                break;
            }
        }
        return triangle;
    }

    public static void print(List<List<Integer>> triangle) {
        StringBuilder sb = new StringBuilder();
        for (List<Integer> line : triangle) {
            for (int i = 0; i < line.size(); i++) {
                sb.append(line.get(i));
                if (i != line.size() - 1) {
                    sb.append(' ');
                }
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

    public static void main(String[] args) {
        print(rollUp(4, 7, 3, 6, 7));
    }
}
