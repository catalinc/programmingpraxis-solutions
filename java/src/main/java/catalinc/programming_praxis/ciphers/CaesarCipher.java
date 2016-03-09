package catalinc.programming_praxis.ciphers;

import java.util.HashMap;

/**
 * @author cata
 */
public class CaesarCipher {

  private static final char[] ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

  private HashMap<Character, Character> cryptTable;
  private HashMap<Character, Character> decryptTable;

  public CaesarCipher(final int shift) {
    if (shift < 0) {
      throw new IllegalArgumentException("shift cannot be negative");
    }
    this.cryptTable = buildTranslationTable(ALPHABET, shift);
    this.decryptTable = buildTranslationTable(ALPHABET, -shift);
  }

  public String crypt(final String plainText) {
    if (plainText == null) {
      throw new IllegalArgumentException("plainText cannot be null");
    }
    return translate(this.cryptTable, plainText);
  }

  public String decrypt(final String encryptedText) {
    if (encryptedText == null) {
      throw new IllegalArgumentException("encryptedText cannot be null");
    }
    return translate(this.decryptTable, encryptedText);
  }

  private HashMap<Character, Character> buildTranslationTable(final char[] alphabet, final int shift) {
    HashMap<Character, Character> translationTable = new HashMap<>(alphabet.length);
    for (int i = 0; i < alphabet.length; i++) {
      Character plain = alphabet[i];
      Character translated = alphabet[mod((i + shift), alphabet.length)];
      translationTable.put(plain, translated);
    }
    return translationTable;
  }

  private String translate(final HashMap<Character, Character> translationTable, final String text) {
    StringBuilder translatedText = new StringBuilder(text.length());
    for (int i = 0; i < text.length(); i++) {
      Character plain = text.charAt(i);
      Character translated = translationTable.get(plain);
      if (translated != null) {
        translatedText.append(translated);
      } else {
        translatedText.append(plain);
      }
    }
    return translatedText.toString();
  }

  private int mod(int a, int b) {
    int r = a % b;
    if (r < 0) {
      r += b;
    }
    return r;
  }

}
