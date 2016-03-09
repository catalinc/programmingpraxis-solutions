package catalinc.programming_praxis.sum;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SumOfTwoSquaresTest {

    @Test
    public void noSolution() {
        assertEquals(0, SumOfTwoSquares.solve(999).size());
    }

    @Test
    public void withSolution() {
        long[][] testData = new long[][] {
                {48612265, 32},
                {50, 2}
        };
        for(long[] testItem : testData) {
            assertEquals(testItem[1], SumOfTwoSquares.solve(testItem[0]).size());
        }
    }
}
