package model;

public class RecordStore {
    private final Albums albums;

    public RecordStore() {
        albums = new Albums();
    }

    public RecordStore(Albums albums) {
        this.albums = albums;
    }

    public Albums getAlbums() {
        return this.albums;
    }
}
