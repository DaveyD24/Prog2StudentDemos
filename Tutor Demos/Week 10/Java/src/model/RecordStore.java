package model;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

import java.util.List;

public class RecordStore {
    private final ObservableList<Album> albums;

    public RecordStore(List<Album> albums) {
        this.albums = FXCollections.observableArrayList(albums);
    }

    public ObservableList<Album> getAlbums() {
        return this.albums;
    }
}