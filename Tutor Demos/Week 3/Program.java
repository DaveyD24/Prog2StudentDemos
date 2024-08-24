import java.util.LinkedList;

/*
 * Specification:
 * Read in names until the user enters "X"
 * Ensure no names have been incorrectly entered with an email address (verified with the inclusion of an @ symbol)
 */

public class Program {

    LinkedList<String> names = new LinkedList<String>();

    private void use() {
        //Merged read-loop pattern
        String name;
        while (!(name = readChoice()).equals("X")) {
            names.add(name);
        }

        //Print whether any emails were spotted
        System.out.println(noEmails() ? "All data validated." : "Email Spotted!");
    }

    private String readChoice() {
        System.out.print("Name: ");
        return In.nextLine();
    }

    //None pattern
    private boolean noEmails() {
        for (String name : names) {
            if (isEmail(name)) {
                return false;
            }
        }
        return true;
    }

    //String-loop pattern
    private boolean isEmail(String name) {
        for (int i = 0; i < name.length(); i++) {
            if (name.charAt(i) == '@') {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        new Program().use();
    }
}