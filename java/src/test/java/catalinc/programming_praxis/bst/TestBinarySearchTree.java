package catalinc.programming_praxis.bst;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class TestBinarySearchTree {
    
    private BinarySearchTree<Integer> bst;

    @Before
    public void setUp() {
        bst = new BinarySearchTree<Integer>();
    }

    @Test
    public void testInsert() {
        bst.insert(1);
        bst.insert(2);
        bst.insert(3);
        assertEquals(3, bst.size());
    }

    @Test
    public void testLookup() {
        bst.insert(100);
        bst.insert(1);
        bst.insert(500);
        bst.insert(1000);
        assertTrue(bst.lookup(1000));
        assertTrue(bst.lookup(1));
    }

    @Test
    public void testDelete() {
        bst.insert(100);
        bst.insert(1);
        bst.insert(10);
        bst.insert(-1);

        bst.delete(0);
        assertEquals(4, bst.size());

        bst.delete(-1);
        bst.delete(1);

        assertEquals(2, bst.size());
        assertTrue(bst.lookup(10));
        assertFalse(bst.lookup(-1));
    }
    
}
