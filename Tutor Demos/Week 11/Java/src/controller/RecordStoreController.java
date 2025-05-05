package controller;

import au.edu.uts.ap.javafx.Controller;
import au.edu.uts.ap.javafx.ViewLoader;
import com.sun.prism.impl.Disposer;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.stage.Stage;
import model.Album;
import model.Albums;
import model.RecordStore;

import java.io.IOException;

public class RecordStoreController extends Controller<RecordStore> {

    @FXML private Button viewBtn;
    @FXML private Button removeBtn;

    @FXML private TableView<Album> albumsTv;
    @FXML private TableColumn<Album, String> artistClm;
    @FXML private TableColumn<Album, String> titleClm;
    @FXML private TableColumn<Album, Integer> stockClm;
    @FXML private TableColumn<Album, Double> priceClm;

    @FXML
    private void initialize() {
        removeBtn.disableProperty().bind(albumsTv.getSelectionModel().selectedItemProperty().isNull());
        viewBtn.disableProperty().bind(albumsTv.getSelectionModel().selectedItemProperty().isNull());

        albumsTv.setItems(model.getAlbums().getAlbums());
        artistClm.setCellValueFactory(cellData -> cellData.getValue().artistProperty());
        titleClm.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        stockClm.setCellValueFactory(cellData -> cellData.getValue().stockProperty().asObject());
        priceClm.setCellValueFactory(cellData -> cellData.getValue().priceProperty().asObject());

        albumsTv.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
        albumsTv.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
    }

    public final RecordStore getRecordStore() {
        return model;
    }

    public Albums getSelectedAlbum() {
        return new Albums(albumsTv.getSelectionModel().getSelectedItems());
    }

    @FXML
    public void handleRemove() {
        for (Album album : getSelectedAlbum().getAlbums()) {
            getRecordStore().getAlbums().remove(album);
        }
    }

    @FXML
    public void handleView() throws IOException {
        for (Album album : getSelectedAlbum().getAlbums()) {
            ViewLoader.showStage(album, "/view/AlbumView.fxml", album.nameProperty().get(), new Stage());
        }
    }

    @FXML
    public void handleClose() {
        Platform.exit();
    }
}
