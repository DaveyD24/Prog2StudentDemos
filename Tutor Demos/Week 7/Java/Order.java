public class Order implements Request{

    private String name;
    private String products;

    public Order(String name, String products) {
        this.name = name;
        this.products = products;
    }

    public String getRequestLine() {
        return this.name + " has requested " + products;
    }

    public void handle() {
        for (String item : products.split(",")) {
            System.out.print("Item: " + item.trim() + ". ");
            char choice = readChoice();
            System.out.println(choice == 'y' ? "Approved" : "Rejected");
        }
    }

    private char readChoice() {
        System.out.print("Approve request? (y/n): ");
        return In.nextChar();
    }
}
