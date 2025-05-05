package model;

import javafx.beans.property.*;

import java.text.DecimalFormat;

public class Album {
    private final StringProperty artist;
    private final StringProperty name;
    private final IntegerProperty stock;
    private final DoubleProperty price;
    private final String imageUrl;

    private final IntegerProperty sold;
    private final DoubleProperty profit;
    private final BooleanProperty available;

    public Album(String artist, String name, int stock, double price, String imageUrl) {
        this.artist = new SimpleStringProperty(artist);
        this.name = new SimpleStringProperty(name);
        this.stock = new SimpleIntegerProperty(stock);
        this.price = new SimpleDoubleProperty(price);
        this.imageUrl = imageUrl;

        this.sold = new SimpleIntegerProperty();
        this.profit = new SimpleDoubleProperty();
        this.available = new SimpleBooleanProperty();
    }

    public ReadOnlyStringProperty artistProperty() {
        return artist;
    }
    public ReadOnlyStringProperty nameProperty() {
        return name;
    }
    public ReadOnlyIntegerProperty stockProperty() {
        return stock;
    }
    public ReadOnlyDoubleProperty priceProperty() {
        return price;
    }
    public String getImageUrl() { return imageUrl; }

    public void sell() {
        stock.set(stock.get()- 1);
        this.sold.set(sold.get() + 1);
        this.profit.set(sold.get() * price.get());
        this.available.set(stock.get() <= 0);
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
        return String.format("%s by %s ($%s)", name, artist, formatted(price.get()));
    }
    private String formatted(double price) {
        return new DecimalFormat("###,##0.00").format(price);
    }
}
