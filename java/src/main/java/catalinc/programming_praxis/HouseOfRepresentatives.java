package catalinc.programming_praxis;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

/**
 * An implementation of Huntington - Hill method.
 */
public class HouseOfRepresentatives {

    private static State[] loadStates(String filename) throws IOException {
        List<State> states = new LinkedList<State>();
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(filename));
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                states.add(new State(parts[0].trim(),
                           Long.parseLong(parts[1].trim()), 1));
            }
        } finally {
            if (br != null) {
                br.close();
            }
        }
        return states.toArray(new State[]{});
    }

    private static double g(double n, double p) {
        return p / Math.sqrt(n * (n + 1));
    }

    public static void compute(String filename, long seats) throws IOException {
        State[] states = loadStates(filename);
        seats -= states.length;
        while (seats > 0) {
            double maxGm = -1;
            int index = -1;
            for (int i = 0; i < states.length; i++) {
                double gm = g(states[i].representatives, states[i].population);
                if (maxGm < gm) {
                    maxGm = gm;
                    index = i;
                }
            }
            states[index].representatives++;
            seats--;
        }
        Arrays.sort(states, new Comparator<State>() {
            public int compare(State o1, State o2) {
                return o2.representatives - o1.representatives;
            }
        });
        int rank = 1;
        for (State state : states) {
            System.out.println(rank + " " + state.name + " "
                    + state.population + " " + " " + state.representatives);
            rank++;
        }
    }

    public static class State {
        private String name;
        private long population;
        private int representatives;

        public State(String name, long population, int representatives) {
            this.name = name;
            this.population = population;
            this.representatives = representatives;
        }
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.err.println("Usage: java catalinc.programming_praxis.HouseOfRepresentatives CENSUS_INPUT_FILE SEATS");
            System.exit(1);
        }
        try {
            compute(args[0], Integer.parseInt(args[1]));
        } catch (IOException e) {
            System.err.println("I/O error: " + e.getMessage());
            System.exit(2);
        }
    }
}
