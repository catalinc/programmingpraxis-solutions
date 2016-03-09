package catalinc.programming_praxis.permuted_index;

import java.io.PrintStream;

/**
 * Pretty printer for permuted index.
 */
public class PrettyPrinter {

    public static void print(PrintStream out, Iterable<SentencePartition> permutedIndex) {
        int maxLenOfSentenceHead = 0;
        for (SentencePartition partition : permutedIndex) {
            int lenOfSentenceHead = partition.getHead().length();
            if (lenOfSentenceHead > maxLenOfSentenceHead) {
                maxLenOfSentenceHead = lenOfSentenceHead;
            }
        }
        for (SentencePartition partition : permutedIndex) {
            out.printf("%" + maxLenOfSentenceHead + "s\t%s\n", partition.getHead(), partition.getTail());
        }
    }
}
