import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.LinkedList;

public class Coach {
    private final Team team;
    private final ArrayList<Team> teams;
    private final Strategy strategy;
    public Coach() {
        this.team = new Team("Hurstville Hornets");
        this.teams = new ArrayList<>();
        teams.add(new Team("Broadway Bulldogs"));
        teams.add(new Team("Olympic Leopards"));
        teams.add(new Team("Chippendale Panthers"));
        teams.add(new Team("West-Broadway Lions"));
        teams.add(new Team("Engadine Sea-Lions"));
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

    private LinkedList<Team> matches(String substring) {
        LinkedList<Team> matches = new LinkedList<Team>();
        for (Team t : teams) {
            if (t.has(substring)) {
                matches.add(t);
            }
        }
        return matches;
    }

    private String readTeam() {
        System.out.print("Team: ");
        return In.nextLine();
    }

    private void play() {

        System.out.println("Enter the team to play against:");
        String sub = readTeam();

        LinkedList<Team> matches = matches(sub);
        if (matches.isEmpty()) {
            System.out.println("No such team in the league");
        }
        else {
            for (Team opponent : matches) {
                playGame(opponent);
            }
        }
    }

    private void playGame(Team opponent) {
        System.out.println("Playing game against " + opponent + " with a focus on " + strategy);
        int result = this.team.play(opponent);

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