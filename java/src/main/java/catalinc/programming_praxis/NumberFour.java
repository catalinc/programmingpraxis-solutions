package catalinc.programming_praxis;

public class NumberFour {

    static StringBuilder numberFourSeq(int n, StringBuilder out) {
        if (n != 4) {
            switch (n % 10) {
                case 0:
                case 4:
                    numberFourSeq(n / 10, out);
                    break;
                default:
                    numberFourSeq(n * 2, out);
            }
            out.append("->");
        }
        out.append(n);
        return out;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java catalinc.programming_praxis.NumberFour NUM1 NUM2...");
            System.exit(1);
        }
        for (String arg : args) {
            System.out.println(numberFourSeq(Integer.parseInt(arg),
                    new StringBuilder()));
        }
    }
}
