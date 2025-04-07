import java.util.LinkedList;
import java.util.Scanner;

public class ReadLoop {

    LinkedList<String> names = new LinkedList<String>();

    private void use() {

        //read pattern
        String val;
        while (!(val = readChoice()).equals("X")) {
            names.add(val);
        }
        if (anyEmptyNames()) {
            System.out.println("Invalid Data!");
        }
    }

    private boolean anyEmptyNames() {
        for (String name : names) {
            if (name.isEmpty()) {
                return true;
            }
        }
        return false;
    }

    private String readChoice() {
        System.out.print("Name: ");
        return In.nextLine();
    }

    public static void main(String[] args) {
        new ReadLoop().use();
    }
}
