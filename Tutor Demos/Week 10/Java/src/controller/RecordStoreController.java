package controller;

import au.edu.uts.ap.javafx.Controller;
import au.edu.uts.ap.javafx.ViewLoader;
import javafx.application.Platform;
import javafx.event.ActionEvent;
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
        albumsLv.setItems(getRecordStore().getAlbums().getAlbums());
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
    public void handleRemove(ActionEvent event) {
        getRecordStore().getAlbums().remove(getSelectedAlbum());
    }

    @FXML
    public void handleView(ActionEvent event) throws IOException {
        ViewLoader.showStage(getSelectedAlbum(), "/view/AlbumView.fxml", getSelectedAlbum().getName(), new Stage());
    }

    @FXML
    public void handleClose(ActionEvent event) {
        Platform.exit();
    }
}