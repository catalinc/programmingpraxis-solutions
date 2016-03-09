package catalinc.programming_praxis.piglatin;

import org.junit.Assert;
import org.junit.Test;

public class PigLatinTest {

    private static String[][] testData =
            new String[][]{
                    {null, null},
                    {"", ""},
                    {"art", "art-way"},
                    {"eagle", "eagle-way"},
                    {"start", "art-stay"},
                    {"door", "oor-day"}
            };

    @Test
    public void translate() {
        for (String[] testItem : testData) {
            Assert.assertEquals(testItem[1],
                    PigLatin.translate(testItem[0]));
        }
    }

    @Test
    public void untranslate() {
        for (String[] testItem : testData) {
            Assert.assertEquals(testItem[0],
                    PigLatin.untranslate(testItem[1]));
        }
    }
}
