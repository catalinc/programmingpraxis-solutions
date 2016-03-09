package catalinc.programming_praxis;

public class CreditCardNumber {

    public static boolean isValid(String s) {
        int sum = 0;
        int count = 1;
        while (count <= s.length()) {
            char ch = s.charAt(s.length() - count);
            int digit = Character.digit(ch, 10);
            if (count % 2 == 0) {
                digit *= 2;
            }
            if (digit >= 10) {
                int q = digit / 10;
                int r = digit % 10;
                sum += q;
                sum += r;
            } else {
                sum += digit;
            }
            count++;
        }
        return sum % 10 == 0;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java catalinc.programming_praxis.CreditCardNumber CARD_NUMBER");
            System.exit(1);
        }
        System.out.println(args[0] + " is " +
                (isValid(args[0]) ? "valid" : "invalid"));
    }
}
