package catalinc.programming_praxis.permuted_index;

import org.junit.Before;
import org.junit.Test;

import java.io.IOException;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class KWICIndexerTest {

    private KWICIndexer indexer;

    @Before
    public void setUp() throws IOException {
        NoiseWordsFilter noiseWordsFilter = new NoiseWordsFilter("/noise_words.lst");
        indexer = new KWICIndexer(noiseWordsFilter);
    }

    @Test
    public void noiseWords() {
        String[] testData = new String[]{
                "a", "an", "the", "AN", "THE"
        };
        for (String testItem : testData) {
            assertEquals(true, indexer.getNoiseWordsFilter().isNoiseWord(testItem));
        }
    }

    @Test
    public void nonNoiseWords() {
        String[] testData = new String[]{
                "cat", "dog", "word", null, ""
        };
        for (String testItem : testData) {
            assertEquals(false, indexer.getNoiseWordsFilter().isNoiseWord(testItem));
        }
    }

    @Test
    public void nullOrEmptySentence() {
        String[] testData = new String[]{
                "", null
        };
        for (String testItem : testData) {
            indexer.addSentence(testItem);
            assertEquals(0, indexer.getIndex().size());
        }
    }

    @Test
    public void resetIndexer() {
        indexer.addSentence("All's well that ends well.");
        indexer.reset();
        assertEquals(0, indexer.getIndex().size());
    }

    @Test
    public void addRemoveSentence() {
        String sentence = "Nature abhors a vacuum.";
        indexer.addSentence(sentence);
        assertEquals(3, indexer.getIndex().size());
        indexer.removeSentence(sentence);
        assertEquals(0, indexer.getIndex().size());
    }

    @Test
    public void buildIndex() {
        String[] sentences = new String[]{
                "All's well that ends well.",
                "Nature abhors a vacuum.",
                "Every man has a price."
        };
        int expectedLines = 12;
        for (String sentence : sentences) {
            indexer.addSentence(sentence);
        }
        List<SentencePartition> index = indexer.getIndex();

        assertEquals(expectedLines, index.size());

        SentencePartition first = index.get(0);
        assertEquals("Nature", first.getHead());
        assertEquals("abhors a vacuum.", first.getTail());

        SentencePartition last = index.get(index.size() - 1);
        assertEquals("All's well that ends", last.getHead());
        assertEquals("well.", last.getTail());
    }
}
