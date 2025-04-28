package controller;

import au.edu.uts.ap.javafx.Controller;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;
import model.Album;

public class AlbumController extends Controller<Album> {

    @FXML private Text albumTxt;
    @FXML private Text artistTxt;
    @FXML private Text soldTxt;
    @FXML private Text profitTxt;
    @FXML private Button buyBtn;
    @FXML private ImageView artView;


    @FXML
    private void initialize() {
        artView.setImage(new Image(getAlbum().getImageUrl()));

        albumTxt.setText(getAlbum().getName());
        artistTxt.setText(getAlbum().getArtist());
        soldTxt.textProperty().bind(getAlbum().soldProperty().asString());
        profitTxt.textProperty().bind(getAlbum().profitProperty().asString("$%.2f"));

        buyBtn.disableProperty().bind(getAlbum().availableProperty());
    }

    public final Album getAlbum() {
        return model;
    }

    @FXML
    public void handlePurchase() {
        getAlbum().sell();
    }

    @FXML
    public void handleClose() {
        stage.close();
    }
}
