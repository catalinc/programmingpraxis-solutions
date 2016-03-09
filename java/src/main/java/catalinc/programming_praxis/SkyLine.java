package catalinc.programming_praxis;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class SkyLine {
    private static class Building {
        private final int start;
        private final int height;
        private final int end;

        private Building(int start, int height, int end) {
            this.start = start;
            this.height = height;
            this.end = end;
        }

        @Override
        public String toString() {
            return "Building{" +
                    "start=" + start +
                    ", height=" + height +
                    ", end=" + end +
                    '}';
        }
    }

    private static List<Building> parseBuildings(String s) {
        List<Building> buildings = new LinkedList<>();
        Scanner scanner = new Scanner(s).useDelimiter("[ \\(\\)]+");
        while (scanner.hasNextInt()) {
            int start = scanner.nextInt();
            int height = scanner.nextInt();
            int end = scanner.nextInt();
            buildings.add(new Building(start, height, end));
        }
        return buildings;
    }

    private static List<Integer> compute(String s) {
        List<Building> buildings = parseBuildings(s);
        int start = buildings.stream().mapToInt(b -> b.start).min().orElse(0);
        int end = buildings.stream().mapToInt(b -> b.end).max().orElse(start);
        List<Integer> skyline = new LinkedList<>();
        int lastHeight = 0;
        for (int i = start; i <= end; i++) {
            final int index = i;
            int height = buildings.stream().filter(b -> b.start <= index && b.end > index).mapToInt(b -> b.height).max().orElse(0);
            if (height != lastHeight) {
                skyline.add(index);
                skyline.add(height);
            }
            lastHeight = height;
        }
        return skyline;
    }

    public static void main(String[] args) {
        String s = "(1 11 5) (2 6 7) (3 13 9) (12 7 16) (14 3 25) (19 18 22) (23 13 29) (24 4 28)";
        System.out.println(SkyLine.compute(s));
    }
}