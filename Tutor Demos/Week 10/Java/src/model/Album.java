package model;

import javafx.beans.binding.Bindings;
import javafx.beans.property.*;

import java.text.DecimalFormat;

public class Album {
    private final String artist;
    private final String name;
    private final IntegerProperty stock;
    private final double price;

    private final IntegerProperty sold;
    private final DoubleProperty profit;

    public Album(String artist, String name, int stock, double price) {
        this.artist = artist;
        this.name = name;
        this.price = price;
        this.stock = new SimpleIntegerProperty(stock);
        this.sold = new SimpleIntegerProperty(0);
        this.profit = new SimpleDoubleProperty(0.0);

        profit.bind(Bindings.multiply(sold, price));
    }

    public String getArtist() {
        return artist;
    }
    public String getName() {
        return name;
    }

    public ReadOnlyIntegerProperty stockProperty() {
        return stock;
    }
    public ReadOnlyIntegerProperty soldProperty() {
        return sold;
    }
    public DoubleProperty profitProperty() {
        return profit;
    }

    public void sell() {
        stock.set(stock.get() - 1);
        sold.set(sold.get() + 1);
    }

    @Override
    public String toString() {
        return name + " by " + artist + " ($" + formatted(price) + ")";
    }

    private String formatted(double price) {
        return new DecimalFormat("#0.00").format(price);
    }
}