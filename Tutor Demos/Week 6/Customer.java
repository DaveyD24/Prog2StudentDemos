import java.util.LinkedList;

/**
 * A customer has a savings account and a loan account.
 *
 * You can deposit into and withdraw from the savings account,
 * and you can transfer money from the savings to the loan account.
 * You can also view the balance of all accounts.
 */
public class Customer {
    public static void main(String[] args) {
        new Customer().use();
    }
    private LinkedList<Account> accounts;

    public Customer() {
        accounts = new LinkedList<Account>();
    }

    public void use() {
        char choice;
        while ((choice = readChoice()) != 'x') {
            switch (choice) {
            case 'a': add(); break;
            case 'r': remove(); break;
            case 'd': deposit(); break;
            case 'w': withdraw(); break;
            case 's': show(); break;
            default: help(); break;
            }
        }
        System.out.println("Done");
    }

    private char readChoice() {
        System.out.print("Customer menu (a/r/d/w/s/x): ");
        return In.nextChar();
    }

    private String readType() {
        System.out.print("Account type: ");
        return In.nextLine();
    }
    private Account account(String type) {
        for (Account a : accounts) {
            if (a.has_type(type)) {
                return a;
            }
        }
        return null;
    }

    private void add() {
        String type = readType();
        Account acc = account(type);
        if (acc != null) {
            System.out.println("Account already exists!");
        }
        else {
            accounts.add(new Account(type));
        }
    }

    private void remove() {
        String type = readType();
        Account acc = account(type);
        if (acc == null) {
            System.out.println("No such account!");
        }
        else {
            accounts.remove(acc);
        }
    }

    private void deposit() {
        Account acc = account(readType());
        if (acc == null) {
            System.out.println("No such account!");
        }
        else {
            acc.deposit(readAmount("deposit"));
        }
    }

    private void withdraw() {
        Account acc = account(readType());
        if (acc == null) {
            System.out.println("No such account!");
        }
        else {
            double amount = readAmount("withdraw");
            if (acc.has(amount))
                acc.withdraw(amount);
            else
                System.out.println("Insufficient funds");
        }
    }

    private double readAmount(String action) {
        System.out.print("Amount to " + action + ": $");
        return In.nextDouble();
    }

    private void show() {
        for (Account a : accounts) {
            System.out.println(a);
        }
    }

    private void help() {
        System.out.println("Menu options");
        System.out.println("d = deposit");
        System.out.println("w = withdraw");
        System.out.println("t = transfer");
        System.out.println("s = show");
        System.out.println("x = exit");
    }
}
