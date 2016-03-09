package catalinc.programming_praxis;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Histogram {

    public static Map<String, Integer> wordFrequency(final File file)
            throws IOException {
        final Map<String, Integer> wordFrequencyMap = new HashMap<String, Integer>();
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(file));
            String line;
            while ((line = br.readLine()) != null) {
                for (String word : line.split("\\W+")) {
                    if (word.length() == 0) {
                        continue;
                    }
                    String lower = word.toLowerCase();
                    if (!wordFrequencyMap.containsKey(lower)) {
                        wordFrequencyMap.put(lower, 1);
                    } else {
                        wordFrequencyMap.put(lower, wordFrequencyMap.get(lower) + 1);
                    }
                }
            }
        } finally {
            if (br != null) {
                br.close();
            }
        }
        return wordFrequencyMap;
    }

    private static String replicate(final String s, final int count) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count; i++) {
            sb.append(s);
        }
        return sb.toString();
    }

    public static void printHistogram(final Map<String, Integer> wordFrequencyMap) {
        if (wordFrequencyMap.isEmpty()) {
            return;
        }
        int maxFreq = 0;
        int maxLen = 0;
        for (Map.Entry<String, Integer> entry : wordFrequencyMap.entrySet()) {
            final int len = entry.getKey().length();
            final int freq = entry.getValue();
            if (maxLen < len) {
                maxLen = len;
            }
            if (maxFreq < freq) {
                maxFreq = freq;
            }
        }
        for (Map.Entry<String, Integer> entry : wordFrequencyMap.entrySet()) {
            final String word = entry.getKey();
            final int freq = entry.getValue();
            System.out.printf("%" + maxLen + "s: %s (%d)\n", word,
                    replicate("#", (freq * 80) / maxFreq), freq);
        }
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java catalinc.programming_praxis.Histogram FILE1 FILE2...");
            System.exit(1);
        }
        for (String filename : args) {
            final File file = new File(filename);
            System.out.println("Processing file: " + file.getAbsolutePath());
            try {
                printHistogram(wordFrequency(file));
            } catch (IOException e) {
                System.err.println("I/O error: " + file.getAbsolutePath());
            }
        }
    }
}
