package model;

import javafx.beans.binding.Bindings;
import javafx.beans.property.*;

import java.text.DecimalFormat;

public class Album {
    private final StringProperty artist;
    private final StringProperty name;
    private final IntegerProperty stock;
    private final DoubleProperty price;

    private final IntegerProperty sold;
    private final DoubleProperty profit;

    public Album(String artist, String name, int stock, double price) {
        this.artist = new SimpleStringProperty(artist);
        this.name = new SimpleStringProperty(name);
        this.price = new SimpleDoubleProperty(price);
        this.stock = new SimpleIntegerProperty(stock);
        this.sold = new SimpleIntegerProperty(0);
        this.profit = new SimpleDoubleProperty(0.0);

        profit.bind(Bindings.multiply(sold, price));
    }

    public String getArtist() {
        return artist.get();
    }
    public String getName() {
        return name.get();
    }

    public StringProperty nameProperty() {
        return name;
    }
    public StringProperty artistProperty() {
        return artist;
    }
    public ReadOnlyIntegerProperty stockProperty() {
        return stock;
    }
    public DoubleProperty priceProperty() {
        return price;
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
        return name + " by " + artist + " ($" + formatted(price.get()) + ")";
    }

    private String formatted(double price) {
        return new DecimalFormat("#0.00").format(price);
    }
}