package catalinc.programming_praxis.ciphers;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import org.junit.Before;
import org.junit.Test;

public class AffineShiftCipherTest {

    private AffineShiftCipher cipher;

    @Before
    public void setUp() {
        cipher = new AffineShiftCipher(new AffineShiftCipher.Key(5, 8));
    }

    @Test
    public void invalidKey() {
        AffineShiftCipher.Key[] invalidKeys = new AffineShiftCipher.Key[]{
                null
        };
        for (AffineShiftCipher.Key key : invalidKeys) {
            try {
                cipher = new AffineShiftCipher(key);
                fail(key + " is invalid");
            } catch (IllegalArgumentException e) {
                // ok
            }
        }
    }

    @Test
    public void encryptNullOrEmptyString() {
        assertEquals(null, cipher.encrypt(null));
        assertEquals("", cipher.encrypt(""));
    }

    @Test
    public void decryptNullOrEmptyString() {
        assertEquals(null, cipher.decrypt(null));
        assertEquals("", cipher.decrypt(""));
    }

    @Test
    public void encryptString() {
        String[][] testData = new String[][]{
                // input, expected
                {"PROGRAMMINGPRAXIS", "FPAMPIQQWVMFPITWU"},
                {"PROGRAMMING PRAXIS !", "FPAMPIQQWVM FPITWU !"}
        };
        for (String[] testItem : testData) {
            assertEquals(testItem[1], cipher.encrypt(testItem[0]));
        }
    }

    @Test
    public void decryptString() {
        String[][] testData = new String[][]{
                // input, expected
                {"FPAMPIQQWVMFPITWU", "PROGRAMMINGPRAXIS"},
                {"FPAMPIQQWVM FPITWU !", "PROGRAMMING PRAXIS !"}
        };
        for (String[] testItem : testData) {
            assertEquals(testItem[1], cipher.decrypt(testItem[0]));
        }
    }

    @Test
    public void encryptDecryptString() {
        String[] testData = new String[]{
                "ABCD", "EFGH", "12AF", "!TF /", "42 WE AG"
        };
        for (String testItem : testData) {
            assertEquals(testItem, cipher.decrypt(cipher.encrypt(testItem)));
        }
    }
}
