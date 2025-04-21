import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;

public class RecordStoreController {
    private RecordStore recordStore = new RecordStore();
    @FXML private Text albumTxt;
    @FXML private Text artistTxt;
    @FXML private Text soldTxt;
    @FXML private Text profitTxt;
    @FXML private Button purchaseBtn;

    @FXML
    private void initialize() {
        albumTxt.setText(recordStore.getAlbum().getName());
        artistTxt.setText(recordStore.getAlbum().getArtist());
        soldTxt.textProperty().bind(recordStore.getAlbum().soldProperty().asString());
        profitTxt.textProperty().bind(recordStore.getAlbum().profitProperty().asString("$%.2f"));
    }

    public final RecordStore getRecordStore() {
        return recordStore;
    }

    @FXML
    public void handlePurchase() {
        recordStore.getAlbum().sell();
        if (recordStore.getAlbum().getStock() == 0) {
            purchaseBtn.setDisable(true);
        }
    }
}
