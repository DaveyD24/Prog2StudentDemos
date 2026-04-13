public class RecordStore {
    private final Album album;

    public RecordStore() {
        this.album = new Album("Stardust", "Serenity", 12, 34.99);
    }

    public final Album getAlbum() {
        return album;
    }
}