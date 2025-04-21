import javafx.beans.property.*;

public class Album {
    private final String artist;
    private final String name;
    private int stock;
    private final double price;

    private IntegerProperty sold;
    private DoubleProperty profit;

    public Album(String artist, String name, int stock, double price) {
        this.artist = artist;
        this.name = name;
        this.stock = stock;
        this.price = price;

        this.sold = new SimpleIntegerProperty(0);
        this.profit = new SimpleDoubleProperty(0.0);
    }

    public String getArtist() {
        return artist;
    }
    public String getName() {
        return name;
    }
    public int getStock() {
        return stock;
    }
    public double getPrice() {
        return price;
    }

    public ReadOnlyIntegerProperty soldProperty() {
        return sold;
    }
    public DoubleProperty profitProperty() {
        return profit;
    }

    //Needed to bind directly through FXML
//    public int getSold() {
//        return sold.get();
//    }
//    public double getProfit() {
//        return profit.get();
//    }

    public void sell() {
        stock-= 1;
        sold.set(sold.get() + 1);
        profit.set(sold.get() * price);
    }

    @Override
    public String toString() {
        return String.format("%s by %s ($%f)", name, artist, price);
    }
}