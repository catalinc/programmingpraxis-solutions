package catalinc.programming_praxis.permuted_index;

import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;

/**
 * Builds Keyword-In-Context (KWIC) index.
 */
public class KWICIndexer {
    private NoiseWordsFilter noiseWordsFilter;
    private List<String> sentences;

    public KWICIndexer(NoiseWordsFilter noiseWordsFilter) {
        this.sentences = new LinkedList<String>();
        this.noiseWordsFilter = noiseWordsFilter;
    }

    public NoiseWordsFilter getNoiseWordsFilter() {
        return noiseWordsFilter;
    }

    public void addSentence(String sentence) {
        sentences.add(sentence);
    }

    public void removeSentence(String sentence) {
        sentences.remove(sentence);
    }

    public void reset() {
        sentences.clear();
    }

    public List<SentencePartition> getIndex() {
        SortedSet<SentencePartition> index = new TreeSet<SentencePartition>(
                new Comparator<SentencePartition>() {
                    public int compare(SentencePartition partition1, SentencePartition partition2) {
                        String tail1 = partition1.getTail().toLowerCase();
                        String tail2 = partition2.getTail().toLowerCase();
                        return tail1.compareTo(tail2);
                    }
                });
        for (String sentence : sentences) {
            index.addAll(buildPartitions(sentence));
        }
        List<SentencePartition> ret = new LinkedList<SentencePartition>();
        ret.addAll(index);
        return ret;
    }

    private  List<SentencePartition> buildPartitions(String sentence) {
        List<SentencePartition> partitions = new LinkedList<SentencePartition>();
        if (sentence != null && sentence.length() > 0) {
            List<String> words = new LinkedList<String>(Arrays.asList(sentence.split("\\s+")));
            SentencePartition lastPartition = new SentencePartition("", join(' ', words));
            partitions.add(lastPartition);
            while (words.size() > 1) {
                String word = words.remove(0);
                String head = (lastPartition.getHead() + " " + word).trim();
                String tail = join(' ', words).trim();
                if (noiseWordsFilter != null && noiseWordsFilter.isNoiseWord(word)) {
                    lastPartition.setHead(head);
                    lastPartition.setTail(tail);
                } else {
                    lastPartition = new SentencePartition(head, tail);
                    partitions.add(lastPartition);
                }
            }
        }
        return partitions;
    }

    private String join(char sep, Iterable<String> words) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            if (sb.length() > 0) {
                sb.append(sep);
            }
            sb.append(word);
        }
        return sb.toString();
    }
}
