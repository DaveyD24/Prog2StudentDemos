import java.text.*;
/**
 * Each account has a type (Savings/Loan) and a balance.
 * The initial balance is read in from the user.
 *
 * You can deposit into and withdraw from an account, and
 * transfer money to another account.
 * In all of these, the amount is read in.
 */
public class Account {
    private String type;
    private double balance;

    public Account(String type) {
        this.type = type;
        balance = readBalance();
    }

    private double readBalance() {
        System.out.print("Initial " + type + " balance: $");
        return In.nextDouble();
    }

    public boolean has(double amount) {
        return balance >= amount;
    }

    public boolean has_type(String type) {
        return this.type.equals(type);
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    @Override
    public String toString() {
        return type + " account has $" + formatted(balance);
    }

    private String formatted(double amount) {
        return new DecimalFormat("###,##0.00").format(amount);
    }
}
