package model;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

public class Albums {
    private final ObservableList<Album> albums;
    public Albums() {
        this.albums = FXCollections.observableArrayList();
    }

    public Albums(ObservableList<Album> albums) {
        this.albums = albums;
    }

    public ObservableList<Album> getAlbums() {
        return albums;
    }

    public void add(Album album) {
        this.albums.add(album);
    }

    public void remove(Album album) {
        this.albums.remove(album);
    }
}
