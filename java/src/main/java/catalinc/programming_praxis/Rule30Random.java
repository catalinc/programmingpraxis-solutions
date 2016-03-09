package catalinc.programming_praxis;

import java.util.Arrays;

public class Rule30Random {

    private boolean[] state;

    public Rule30Random(int seed) {
        this.state = new boolean[31];
        int i = 0;
        while (seed != 0) {
            state[i] = seed % 2 == 1;
            seed /= 2;
            i++;
        }
    }

    public int next() {
        boolean[] randomBits = new boolean[31];
        for (int i = 0; i < 31; i++) {
            boolean[] nextState = new boolean[state.length];
            for (int j = 0; j < state.length; j++) {
                boolean[] prev = new boolean[3];
                prev[2] = state[j == 0 ? state.length - 1 : j - 1];
                prev[1] = state[j];
                prev[0] = state[j == state.length - 1 ? 0 : j + 1];
                int value = intFromBits(prev);
                switch (value) {
                    case 7:
                    case 6:
                    case 5:
                    case 0:
                        nextState[j] = false;
                        break;
                    case 4:
                    case 3:
                    case 2:
                    case 1:
                        nextState[j] = true;
                        break;
                    default:
                        throw new RuntimeException("unknown rule " + Arrays.toString(prev));
                }
            }
            state = nextState;
            randomBits[i] = state[0];
        }
        return intFromBits(randomBits);
    }

    private int intFromBits(boolean[] bits) {
        int intValue = 0;
        for (int i = 0; i < bits.length && i < 31; i++) {
            if (bits[i]) {
                intValue += pow2(i);
            }
        }
        return intValue;
    }

    private int pow2(int exp) {
        int value = 1;
        for (int i = 0; i < exp; i++) {
            value *= 2;
        }
        return value;
    }

    public static void main(String[] args) {
        if (args.length < 2) {
            System.err.println("Usage: java catalinc.programming_praxis.Rule30Random SEED COUNT");
            System.exit(1);
        }
        int seed = Integer.parseInt(args[0]);
        int count = Integer.parseInt(args[1]);
        Rule30Random rnd = new Rule30Random(seed);
        for (int i = 0; i < count; i++) {
            System.out.println("Random#" + i + ": " + rnd.next());
        }
    }
}
