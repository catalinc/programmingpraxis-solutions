package catalinc.programming_praxis.ciphers;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * @author cata
 */
public class CaesarCipherTest {

  @Test(expected = IllegalArgumentException.class)
  public void testNegativeShift() {
    new CaesarCipher(-1);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testCryptNull() {
    new CaesarCipher(1).crypt(null);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testDecryptNull() {
    new CaesarCipher(1).decrypt(null);
  }

  @Test
  public void testEmpty() {
    CaesarCipher cipher = new CaesarCipher(3);

    assertEquals("", cipher.crypt(""));
    assertEquals("", cipher.decrypt(""));
  }

  @Test
  public void testNonAlphabetCharacters() {
    CaesarCipher cipher = new CaesarCipher(3);

    String text = "#@!<>";

    assertEquals(text, cipher.crypt(text));
    assertEquals(text, cipher.decrypt(text));
  }

  @Test
  public void testCrypt() {
    CaesarCipher cipher = new CaesarCipher(3);

    assertEquals("SURJUDPPLQJSUDALV", cipher.crypt("PROGRAMMINGPRAXIS"));
  }

  @Test
  public void testDecrypt() {
    CaesarCipher cipher = new CaesarCipher(3);

    assertEquals("PROGRAMMINGPRAXIS", cipher.decrypt("SURJUDPPLQJSUDALV"));
  }

}
