package controller;

import au.edu.uts.ap.javafx.Controller;
import au.edu.uts.ap.javafx.ViewLoader;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;
import javafx.stage.Stage;
import model.Album;
import model.RecordStore;

import java.io.IOException;

public class RecordStoreController extends Controller<RecordStore> {

    @FXML private ListView<Album> albumsLv;
    @FXML private Button viewBtn;
    @FXML private Button removeBtn;

    @FXML
    private void initialize() {
        albumsLv.setItems(model.getAlbums().getAlbums());
        removeBtn.disableProperty().bind(albumsLv.getSelectionModel().selectedItemProperty().isNull());
        viewBtn.disableProperty().bind(albumsLv.getSelectionModel().selectedItemProperty().isNull());
    }

    public final RecordStore getRecordStore() {
        return model;
    }

    public Album getSelectedAlbum() {
        return albumsLv.getSelectionModel().getSelectedItem();
    }

    @FXML
    public void handleRemove() {
        Album selectedAlbum = getSelectedAlbum();
        if (selectedAlbum != null) {
            model.getAlbums().remove(selectedAlbum);
        }
    }

    @FXML
    public void handleView() throws IOException {
        if (getSelectedAlbum() != null) {
            ViewLoader.showStage(getSelectedAlbum(), "/view/AlbumView.fxml", getSelectedAlbum().getName(), new Stage());
        }
    }

    @FXML
    public void handleClose() {
        Platform.exit();
    }
}
