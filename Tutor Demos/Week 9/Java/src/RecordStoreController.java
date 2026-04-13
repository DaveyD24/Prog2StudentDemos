import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.text.Text;

public class RecordStoreController {
    private final RecordStore recordStore = new RecordStore();
    @FXML private Text albumTxt;
    @FXML private Text artistTxt;
    @FXML private Text soldTxt;
    @FXML private Text profitTxt;
    @FXML private Button purchaseBtn;

    @FXML
    private void initialize() {
        albumTxt.setText(getRecordStore().getAlbum().getName());
        artistTxt.setText(getRecordStore().getAlbum().getArtist());
        soldTxt.textProperty().bind(getRecordStore().getAlbum().soldProperty().asString());
        profitTxt.textProperty().bind(getRecordStore().getAlbum().profitProperty().asString("$%.2f"));
        purchaseBtn.disableProperty().bind(getRecordStore().getAlbum().stockProperty().isEqualTo(0));
    }

    public final RecordStore getRecordStore() {
        return recordStore;
    }

    @FXML
    public void handlePurchase(ActionEvent event) {
        recordStore.getAlbum().sell();
    }
}