public class RecordStore {
    private final Album album;

    public RecordStore() {
        this.album = new Album("TWICE", "Ready To Be", 12, 34.99);
    }

    public final Album getAlbum() {
        return album;
    }
}