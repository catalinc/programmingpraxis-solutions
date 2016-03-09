package catalinc.programming_praxis;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class TuringMachine {
    private int head;
    private int state;
    private List<Instruction> program;

    private static class Instruction {
        int state;
        String input;
        String output;
        char direction;
        int nextState;

        private Instruction(int state, String input, String output,
                            char direction, int nextState) {
            this.state = state;
            this.input = input;
            this.output = output;
            this.direction = direction;
            this.nextState = nextState;
        }
    }

    public void loadProgram(String filename) throws FileNotFoundException {
        FileInputStream in = new FileInputStream(filename);
        Scanner sc = new Scanner(in);
        program = new LinkedList<Instruction>();
        while (sc.hasNextLine()) {
            Scanner sc2 = new Scanner(sc.nextLine());
            program.add(new Instruction(sc2.nextInt(),  // state
                    sc2.next(),     // input
                    sc2.next(),     // output
                    sc2.next().charAt(0),   // direction
                    sc2.nextInt()));        // next state
        }
    }

    public void execute(String input) {
        String[] tape = input.split("\\s+");
        placeHead(tape);
        state = 0;
        while (state >= 0) {
            for (Instruction instr : program) {
                if (instr.state == state && instr.input.equals(tape[head])) {
                    tape[head] = instr.output;
                    state = instr.nextState;
                    switch (instr.direction) {
                        case 'R':
                            head++;
                            break;
                        case 'L':
                            head--;
                            break;
                        default:
                            throw new RuntimeException("Invalid direction: " + instr.direction);
                    }
                    if (head < 0 || head >= tape.length) {
                        throw new RuntimeException("Invalid tape position: " + head);
                    }
                }
            }
        }
        tape[head] = "[" + tape[head] + "]";
        System.out.println(join(tape, " "));
    }

    private void placeHead(String[] tape) {
        for (int i = 0; i < tape.length; i++) {
            if (tape[i].startsWith("[")) {
                head = i;
                tape[i] = tape[i].replaceAll("\\[|\\]", "");
                return;
            }
        }
        throw new RuntimeException("Unable to place head");
    }

    private String join(String[] arr, String sep) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
            if (i != arr.length - 1) {
                sb.append(sep);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        TuringMachine tm = new TuringMachine();
        try {
            tm.loadProgram("adder.tm");
            tm.execute("_ _ _ [1] 1 1 + 1 1 1 1 1 _ _ _");
        } catch (FileNotFoundException e) {
            System.err.println("File not found: " + e.getMessage());
        }
    }
}
