package model;

import javafx.beans.property.*;

import java.text.DecimalFormat;

public class Album {
    private final String artist;
    private final String name;
    private int stock;
    private final double price;
    private final String imageUrl;

    private final IntegerProperty sold;
    private final DoubleProperty profit;
    private final BooleanProperty available;

    public Album(String artist, String name, int stock, double price, String imageUrl) {
        this.artist = artist;
        this.name = name;
        this.stock = stock;
        this.price = price;
        this.imageUrl = imageUrl;

        this.sold = new SimpleIntegerProperty();
        this.profit = new SimpleDoubleProperty();
        this.available = new SimpleBooleanProperty();
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
    public String getImageUrl() { return imageUrl; }

    public void sell() {
        stock -= 1;
        this.sold.set(sold.get() + 1);
        this.profit.set(sold.get() * price);
        this.available.set(stock <= 0);
    }

    public ReadOnlyIntegerProperty soldProperty() {
        return sold;
    }

    public ReadOnlyDoubleProperty profitProperty() {
        return profit;
    }

    public ReadOnlyBooleanProperty availableProperty() {
        return available;
    }

    @Override
    public String toString() {
        return String.format("%s by %s ($%s)", name, artist, formatted(price));
    }

    private String formatted(double price) {
        return new DecimalFormat("###,##0.00").format(price);
    }
}
