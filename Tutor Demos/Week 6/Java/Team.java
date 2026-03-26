import java.util.ArrayList;
import java.util.Random;

public class Team {
    private final String localName;
    private final String teamName;
    private final ArrayList<Integer> results;
    private final Random random;

    public Team(String name) {
        this.localName = name.split(" ")[0];
        this.teamName = name.split(" ")[1];
        this.results = new ArrayList<>();
        this.random = new Random();
    }

    public int play(Team opponent) {
        int result = random.nextInt(91) * (random.nextBoolean() ? 1 : -1);
        this.addResult(result);
        opponent.addResult(result*-1);
        return result;
    }

    private void addResult(int result) {
        results.add(result);
    }

    public int best() {
        if (noWins()) {
            return 0;
        }
        int max = Integer.MIN_VALUE;
        for (Integer result : results) {
            if (result > max) {
                max = result;
            }
        }
        return max;
    }

    public int worst() {
        if (noLosses()) {
            return 0;
        }
        int min = Integer.MAX_VALUE;
        for (Integer result : results) {
            if (result < min) {
                min = result;
            }
        }
        return min;
    }

    private boolean noWins() {
        for (int result : results) {
            if (result > 0) {
                return false;
            }
        }
        return true;
    }

    private boolean noLosses() {
        for (int result : results) {
            if (result < 0) {
                return false;
            }
        }
        return true;
    }

    public boolean has(String substring) {
        return localName.toLowerCase().contains(substring.toLowerCase()) || teamName.toLowerCase().contains(substring.toLowerCase());
    }

    public double average() {
        if (results.isEmpty()) {
            return 0;
        }
        int sum = 0;
        for (Integer result : results) {
            sum += result;
        }
        return (double)sum/results.size();
    }

    @Override
    public String toString() {
        return localName + " " + teamName;
    }
}