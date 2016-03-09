package catalinc.programming_praxis;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collection;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.SortedMap;
import java.util.TreeMap;

public class XRef {

    public static boolean isJavaIdentifier(String s) {
        if (s.length() == 0 || !Character.isJavaIdentifierStart(s.charAt(0))) {
            return false;
        }
        for (int i = 1; i < s.length(); i++) {
            if (!Character.isJavaIdentifierPart(s.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    public static SortedMap<String, List<Integer>> build(File source)
            throws FileNotFoundException {
        SortedMap<String, List<Integer>> xref = new TreeMap<String, List<Integer>>();
        Scanner sc = null;
        try {
            sc = new Scanner(source);
            int lineCount = 0;
            boolean multiLineComment = false;
            while (sc.hasNextLine()) {
                lineCount++;
                Scanner sc2 = new Scanner(sc.nextLine());
                boolean singleLineComment = false;
                while (sc2.hasNext()) {
                    String token = sc2.next();
                    if (!multiLineComment && token.startsWith("//")) {
                        singleLineComment = true;
                    } else if (!singleLineComment && token.startsWith("/*")) {
                        multiLineComment = true;
                    } else if (multiLineComment && token.startsWith("*/")) {
                        multiLineComment = false;
                    } else if (!singleLineComment &&
                            !multiLineComment &&
                            isJavaIdentifier(token)) {
                        if (!xref.containsKey(token)) {
                            xref.put(token, new LinkedList<Integer>());
                        }
                        xref.get(token).add(lineCount);
                    }
                }
            }
        } finally {
            if (sc != null) {
                sc.close();
            }
        }

        return xref;
    }

    private static String join(Collection<?> c) {
        StringBuilder sb = new StringBuilder();
        for (Iterator<?> it = c.iterator(); it.hasNext();) {
            Object o = it.next();
            sb.append(o);
            if (it.hasNext()) {
                sb.append(", ");
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java catalinc.programming_praxis.XRef FILE1 FILE2...");
            System.exit(1);
        }
        for (String filename : args) {
            File file = new File(filename);
            System.out.println("Processing file: " + file.getAbsolutePath());
            try {
                SortedMap<String, List<Integer>> xref = build(file);
                for (Map.Entry<String, List<Integer>> entry : xref.entrySet()) {
                    System.out.println(entry.getKey() + " " + join(entry.getValue()));
                }
            } catch (FileNotFoundException e) {
                System.err.println("File not found: " + file.getAbsolutePath());
            }
        }
    }
}
