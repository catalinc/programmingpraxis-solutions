package catalinc.programming_praxis.permuted_index;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * Filter for certain 'noise words' like <i>a, an, the</i> etc.
 */
public class NoiseWordsFilter {
    private Set<String> words;

    public NoiseWordsFilter(String filePath) throws IOException {
        loadWords(filePath);
    }

    public void loadWords(String filePath) throws IOException {
        words = new HashSet<String>();
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(
                    new InputStreamReader(
                            NoiseWordsFilter.class.getResourceAsStream(filePath)));
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim().toLowerCase();
                if (line.length() > 0 && !line.startsWith("#")) {
                    words.add(line);
                }
            }
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    // empty
                }
            }
        }
    }

    public boolean isNoiseWord(String word) {
        return word != null && words.contains(word.toLowerCase());
    }
}
