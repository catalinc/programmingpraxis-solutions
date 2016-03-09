package catalinc.programming_praxis;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Scanner;
import java.util.Stack;

public class RPNCalculator {

    static void repl(Reader in) throws IOException {
        BufferedReader br = new BufferedReader(in);
        Stack<Double> stack = new Stack<Double>();
        String line;
        try {
            while ((line = br.readLine()) != null) {
                Scanner sc = new Scanner(line);
                while (sc.hasNext()) {
                    if (sc.hasNextDouble()) {
                        stack.push(sc.nextDouble());
                    } else {
                        char op = sc.next().charAt(0);
                        if (stack.size() < 2) {
                            throw new RuntimeException("unexpected operator: " + op);
                        }
                        double right = stack.pop();
                        double left = stack.pop();
                        switch (op) {
                            case '+':
                                stack.push(left + right);
                                break;
                            case '-':
                                stack.push(left - right);
                                break;
                            case '*':
                                stack.push(left * right);
                                break;
                            case '/':
                                stack.push(left / right);
                                break;
                            default:
                                throw new RuntimeException("invalid input: " + op);
                        }
                    }
                }
                System.out.println("> " + stack.pop());
            }
        } finally {
            try {
                br.close();
            } catch (IOException e) {
                // empty
            }
        }
    }

    public static void main(String[] args) {
        try {
            RPNCalculator.repl(new InputStreamReader(System.in));
        } catch (IOException e) {
            System.out.println("I/O error: " + e.getMessage());
        }
    }
}
