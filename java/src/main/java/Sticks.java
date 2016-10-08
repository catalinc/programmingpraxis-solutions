import java.util.PriorityQueue;

/**
 * Solution to https://programmingpraxis.com/2016/10/07/sticks/
 */
public class Sticks {
    public int solve(int[] sticks) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n: sticks) {
            pq.add(n);
        }
        int cost = 0;
        while (pq.size() > 1) {
            int combined = pq.poll() + pq.poll();
            cost += combined;
            pq.add(combined);
        }
        return cost;
    }
}
