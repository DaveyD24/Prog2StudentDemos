import java.util.LinkedList;

public class SaleManager {
    LinkedList<Integer> sales; 
    static int costPerSale = 10;

    public SaleManager() {
        sales = new LinkedList<Integer>();
    }

    public void sale(int x) {
        sales.add(x);
    }

    public boolean profitable() {
        int gross = 0;
        for (int sale : sales) {
            gross += sale;
        }
        int loss = sales.size() * costPerSale;
        boolean isProfitable = gross > loss;
        if (!isProfitable) {
            costPerSale -= 1;
        }
        return isProfitable;
    }

    public static void main(String[] args) {
        
    }
}