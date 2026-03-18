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

    public int play() {
        int result = random.nextInt(91) * (random.nextBoolean() ? 1 : -1);
        results.add(result);
        return result;
    }

    public int best() {
        //No checks
        int max = Integer.MIN_VALUE;
        for (Integer result : results) {
            if (result > max) {
                max = result;
            }
        }
        return max;
    }

    public int worst() {
        //No checks
        int min = Integer.MAX_VALUE;
        for (Integer result : results) {
            if (result < min) {
                min = result;
            }
        }
        return min;
    }

    public double average() {
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