package catalinc.programming_praxis;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Scanner;

/**
 * An implementation for original Unix V7 fortune program.
 */
public class Fortune {

    public static String getFortune(String filename) throws FileNotFoundException {
        InputStream is = new FileInputStream(filename);
        Scanner sc = new Scanner(is);
        String sel = null;
        double p = 0;
        while(sc.hasNextLine()) {
            String line = sc.nextLine();
            p++;
            if (Math.random() < 1.0 / p) {
                sel = line;
            }
        }
        return sel;
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: java catalinc.programming_praxis.Fortune COOKIE_JAR_FILE");
            System.exit(1);
        }
        try {
            System.out.println(getFortune(args[0]));
        } catch (FileNotFoundException e) {
            System.err.println(args[0] + " not found");
        }
    }
}
