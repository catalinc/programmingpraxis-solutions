package catalinc.programming_praxis;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Solution to http://programmingpraxis.com/2014/12/16/find-two-added-integers/
 */
public class TwoAddedIntegers {

    public static List<Integer> difference(List<Integer> l1, List<Integer> l2) {
        Set<Integer> common = new HashSet<>(l2);
        return l1.stream().filter(n -> !common.contains(n)).collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<Integer> l1 = Arrays.asList(1, 4, 9, 2, 7, 3);
        List<Integer> l2 = Arrays.asList(9, 7, 4, 1);
        System.out.println(difference(l1, l2));
    }
}
