import java.util.LinkedList;

public class CoffeeShop {
    private LinkedList<Request> requests;

    public CoffeeShop() {
        this.requests = new LinkedList<Request>();
        requests.add(new Order("David", "4 packs of coffee, 1 large cappucino"));
        requests.add(new PartnershipOffer("David"));
        requests.add(new Order("Jenny", "5 packs of coffee, 1 medium latte, 1 medium flat white"));
        requests.add(new PartnershipOffer("Jenny"));
        requests.add(new Order("Daisy", "2 packs of coffee, 1 large latte"));
    }

    private void use() {
        for (Request r : requests) {
            System.out.println(r.getRequestLine());
            r.handle();
        }
    }

    public static void main(String[] args) {
        CoffeeShop shop = new CoffeeShop();
        shop.use();
    }
}
