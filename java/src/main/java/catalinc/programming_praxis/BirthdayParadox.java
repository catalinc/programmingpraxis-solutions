package catalinc.programming_praxis;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class BirthdayParadox {

    private static final Random randGen = new Random();

    static float simulate(int nPeople, int nTrials) {
        int n = 0;
        for(int i = 0; i < nTrials; i++) {
            if(trial(nPeople)) n++;
        }
        return (float)n/nTrials;
    }

    static boolean trial(int nPeople) {
        Set<Integer> birthdays = new HashSet<Integer>();
        for (int i = 0; i < nPeople; i++) {
            int day = randGen.nextInt(365);
            if (birthdays.contains(day)) return true;
            birthdays.add(day);
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.printf("%.4f\n", simulate(23, 1000));
        System.out.printf("%.4f\n", simulate(57, 1000));
    }
}
