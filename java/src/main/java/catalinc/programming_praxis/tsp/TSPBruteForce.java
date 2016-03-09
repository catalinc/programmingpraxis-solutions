package catalinc.programming_praxis.tsp;

import catalinc.programming_praxis.PermutationGenerator;

import java.util.LinkedList;
import java.util.List;
import java.util.Random;

/**
 * Traveling salesman problem.
 */
public class TSPBruteForce {

    static class Point {
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static List<Point> randomPoints(int count, int minX, int maxX,
                                    int minY, int maxY) {
        List<Point> points = new LinkedList<Point>();
        Random rnd = new Random();
        for (int i = 0; i < count; i++) {
            int x = minX + rnd.nextInt(maxX + 1);
            int y = minY + rnd.nextInt(maxY + 1);
            points.add(new Point(x, y));
        }
        return points;
    }

    static double distance(Point a, Point b) {
        int dx = b.x - a.x;
        int dy = b.y - a.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    static double tourLength(List<Point> points) {
        double length = 0.0;
        for (int i = 0; i < points.size() - 1; i++) {
            length += distance(points.get(i), points.get(i + 1));
        }
        length += distance(points.get(0), points.get(points.size() - 1));
        return length;
    }

    // because we can :-)
    public static void bruteForce(List<Point> points) {
        PermutationGenerator perm = new PermutationGenerator(points.size());
        List<Point> bestTour = null;
        double bestLength = Double.MAX_VALUE;
        long start = System.currentTimeMillis();
        while (perm.hasMore()) {
            int[] p = perm.getNext();
            List<Point> tour = new LinkedList<Point>();
            for (int i = 0; i < p.length; i++) {
                tour.add(points.get(p[i]));
            }
            double tourLength = tourLength(tour);
            if (bestLength > tourLength) {
                bestLength = tourLength;
                bestTour = tour;
            }
        }
        long end = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder("Best tour: ");
        for (Point p : bestTour) {
            sb.append("(")
              .append(p.x)
              .append(",")
              .append(p.y)
              .append(") ");
        }
        sb.append("Length: ").append(bestLength);
        sb.append(" Time: ").append(end - start).append(" msec");
        System.out.println(sb);
    }

    public static void main(String[] args) {
        bruteForce(randomPoints(10, 0, 100, 0, 100));
    }
}
