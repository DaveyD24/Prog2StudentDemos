public class PartnershipOffer implements Request {

    private String name;

    public PartnershipOffer(String name) {
        this.name = name;
    }

    public String getRequestLine() {
        return this.name + " has requested to do business with you";
    }

    public void handle() {
        char choice = readChoice();
        System.out.println(choice == 'y' ? "Approved" : "Rejected");
    }

    private char readChoice() {
        System.out.print("Approve request? (y/n): ");
        return In.nextChar();
    }
}