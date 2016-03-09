package catalinc.programming_praxis.tsp;

import java.awt.*;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

import static java.lang.Math.random;
import static java.lang.Math.sqrt;

/**
 * Traveling salesman problem. Nearest neighbor solution.
 */
public class TSPNearestNeighbour {

    List<Point> solveNearestNeighbor(List<Point> circuit) {
        List<Point> shortestCircuit = new LinkedList<Point>();
        Point current = circuit.remove(0);
        shortestCircuit.add(current);
        while (!circuit.isEmpty()) {
            Point nearest = getNearest(current, circuit);
            circuit.remove(nearest);
            shortestCircuit.add(nearest);
            current = nearest;
        }
        return shortestCircuit;
    }

    double circuitLength(List<Point> circuit) {
        double len = 0;
        for (int i = 1; i < circuit.size(); i++) {
            len += distance(circuit.get(i), circuit.get(i - 1));
        }
        if (circuit.size() >= 2) {
            len += distance(circuit.get(circuit.size() - 1), circuit.get(0));
        }
        return len;
    }

    Point getNearest(Point p, List<Point> others) {
        double bestDistance = Double.MAX_VALUE;
        Point nearest = null;
        for (Point other : others) {
            double distance = distance(p, other);
            if (distance <= bestDistance) {
                bestDistance = distance;
                nearest = other;
            }
        }
        return nearest;
    }

    double distance(Point a, Point b) {
        double dx = a.getX() - b.getX();
        double dy = a.getY() - b.getY();
        return sqrt(dx * dx + dy * dy);
    }

    Point randomPoint(double maxX, double maxY) {
        Point p = new Point();
        p.setLocation(random() * maxX, random() * maxY);
        return p;
    }

    List<Point> randomCircuit(int size, int maxX, int maxY) {
        List<Point> circuit = new LinkedList<Point>();
        for (int i = 0; i < size; i++) {
            circuit.add(randomPoint(maxX, maxY));
        }
        return circuit;
    }

    void printCircuit(List<Point> circuit) {
        System.out.println("Circuit: ");
        for (Iterator<Point> iterator = circuit.iterator(); iterator.hasNext();) {
            Point point = iterator.next();
            System.out.print("(" + point.getX() + ", " + point.getY() + ")");
            if (iterator.hasNext()) {
                System.out.print(" -> ");
            }
        }
        System.out.println("\nTotal path length: " + circuitLength(circuit));
    }

    public static void main(String[] args) {
        TSPNearestNeighbour tsp = new TSPNearestNeighbour();
        System.out.println("* Initial circuit *");
        List<Point> circuit = tsp.randomCircuit(10, 100, 100);
        tsp.printCircuit(circuit);
        System.out.println("* Solution *");
        tsp.printCircuit(tsp.solveNearestNeighbor(circuit));
    }
}
