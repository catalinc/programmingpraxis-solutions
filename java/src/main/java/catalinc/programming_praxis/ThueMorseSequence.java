package catalinc.programming_praxis;

import java.util.LinkedList;
import java.util.List;

public class ThueMorseSequence {

    public static List<Integer> compute(int nth) {
        List<Integer> sequence = new LinkedList<>();
        sequence.add(0);
        for (int i = 1; i <= nth; i++) {
            int sz = sequence.size();
            for (int j = 0; j < sz; j++) {
                sequence.add(sequence.get(j) == 1 ? 0 : 1);
            }
        }
        return sequence;
    }

    public static void main(String[] args) {
        System.out.println(ThueMorseSequence.compute(8));
    }
}
