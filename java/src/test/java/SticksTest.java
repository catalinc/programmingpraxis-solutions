import org.junit.Test;

import static org.junit.Assert.*;

public class SticksTest {
    @Test
    public void emptyInput() throws Exception {
        Sticks solver = new Sticks();
        assertEquals(0, solver.solve(new int[]{}));
    }

    @Test
    public void solve() {
        Sticks solver = new Sticks();
        assertEquals(10, solver.solve(new int[]{1, 2, 4}));
    }
}