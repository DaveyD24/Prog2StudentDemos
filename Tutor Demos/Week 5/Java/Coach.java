import java.text.DecimalFormat;

public class Coach {
    private final Team team;
    private final Strategy strategy;
    public Coach() {
        this.team = new Team("Hurstville Hornets");
        this.strategy = new Strategy();
    }

    private void use() {
        char choice;
        while ((choice = readChoice()) != 'x') {
            switch (choice) {
                case 'p': play(); break;
                case 't': viewStats(); break;
                case 's': viewStrategy(); break;
                default: help(); break;
            }
        }
    }
    private char readChoice() {
        System.out.print("Choice (p/t/s/x): ");
        return In.nextChar();
    }

    private void play() {
        System.out.println("Playing game with a focus on " + strategy);
        int result = team.play();

        //ignoring draws
        if (result >= 0) {
            System.out.println("Game won by " + result + " points");
        }
        else {
            System.out.println("Game lost by " + (result*-1) + " points");
        }

        if (result <= -20) {
            strategy.changeStrategy();
        }
    }

    private void viewStats() {
        System.out.println("Statistics for " + team);
        System.out.println("Biggest win: " + team.best());
        System.out.println("Biggest loss: " + team.worst());
        System.out.println("Average margin: " + formatted(team.average()));
    }

    private void viewStrategy() {
        System.out.println("Current strategy for " + team + ": " + strategy);
    }

    private String formatted(double score) {
        return new DecimalFormat("#0.00").format(score);
    }

    private void help() {
        System.out.println("Menu options:");
        System.out.println("p = play game");
        System.out.println("t = team stats");
        System.out.println("s = current strategy");
    }

    public static void main(String[] args) {
        Coach coach = new Coach();
        coach.use();
    }
}