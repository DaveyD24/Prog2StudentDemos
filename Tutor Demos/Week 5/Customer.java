public class Customer {
    public static void main(String[] args) {
        new Customer().use();
    }
    private Account savingsAccount;
    private Account loanAccount;

    public Customer() {
        savingsAccount = new Account(AccountType.SAVINGS);
        loanAccount = new Account(AccountType.LOAN);
    }

    public void use() {
        char choice;
        while ((choice = readChoice()) != 'x') {
            switch (choice) {
            case 'd': deposit(); break;
            case 'w': withdraw(); break;
            case 't': transfer(); break;
            case 's': show(); break;
            default: help(); break;
            }
        }
        System.out.println("Done");
    }

    private char readChoice() {
        System.out.print("Customer menu (d/w/t/s/x): ");
        return In.nextChar();
    }

    private void deposit() {
        savingsAccount.deposit(readAmount("deposit"));
    }

    private void withdraw() {
        double amount = readAmount("withdraw");
        if (savingsAccount.has(amount))
            savingsAccount.withdraw(amount);
        else
            System.out.println("Insufficient funds");
    }

    private void transfer() {
        double amount = readAmount("transfer");
        if (savingsAccount.has(amount))
            savingsAccount.transferTo(amount, loanAccount);
        else
            System.out.println("Insufficient funds");
    }

    private double readAmount(String action) {
        System.out.print("Amount to " + action + ": $");
        return In.nextDouble();
    }

    private void show() {
        System.out.println(savingsAccount);
        System.out.println(loanAccount);
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
