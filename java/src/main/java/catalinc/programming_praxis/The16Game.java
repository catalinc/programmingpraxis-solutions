package catalinc.programming_praxis;

import java.util.ArrayList;
import java.util.Collections;

public class The16Game {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.printf("usage: %s NUM_SIMULATIONS\n", The16Game.class.getName());
            System.exit(1);
        }
        int n = Integer.parseInt(args[0]);
        int wins = 0;
        for (int i = 0; i < n; i++) {
            if (simulate()) {
                wins++;
            }
        }
        System.out.printf("%d wins out of %d tries [%.2f wining percentage]\n", wins, n, ((float) wins / n) * 100);
    }

    private static boolean simulate() {
        ArrayList<Integer> card = new ArrayList<>(16);
        for (int i = 1; i <= 16; i++) {
            card.add(i);
        }
        Collections.shuffle(card);
        return card.indexOf(3) > card.indexOf(1) && card.indexOf(3) > card.indexOf(2);
    }
}
