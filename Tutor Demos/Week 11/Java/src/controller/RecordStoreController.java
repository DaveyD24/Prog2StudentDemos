package controller;

import au.edu.uts.ap.javafx.Controller;
import au.edu.uts.ap.javafx.ViewLoader;
import javafx.application.Platform;
import javafx.event.ActionEvent;
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
    @FXML private TableColumn<Album, String> artistCol;
    @FXML private TableColumn<Album, String> titleCol;
    @FXML private TableColumn<Album, Integer> stockCol;
    @FXML private TableColumn<Album, Double> priceCol;

    @FXML
    private void initialize() {
        removeBtn.disableProperty().bind(albumsTv.getSelectionModel().selectedItemProperty().isNull());
        viewBtn.disableProperty().bind(albumsTv.getSelectionModel().selectedItemProperty().isNull());

        albumsTv.setItems(getRecordStore().getAlbums().getAlbums());
        artistCol.setCellValueFactory(cellData -> cellData.getValue().artistProperty());
        titleCol.setCellValueFactory(cellData -> cellData.getValue().nameProperty());
        stockCol.setCellValueFactory(cellData -> cellData.getValue().stockProperty().asObject());
        priceCol.setCellValueFactory(cellData -> cellData.getValue().priceProperty().asObject());

        albumsTv.setColumnResizePolicy(TableView.CONSTRAINED_RESIZE_POLICY);
        albumsTv.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
    }

    public final RecordStore getRecordStore() {
        return model;
    }

    public Albums getSelectedAlbums() {
        return new Albums(albumsTv.getSelectionModel().getSelectedItems());
    }

    @FXML
    public void handleRemove(ActionEvent event) {
        for (Album album : getSelectedAlbums().getAlbums()) {
            getRecordStore().getAlbums().remove(album);
        }
    }

    @FXML
    public void handleView(ActionEvent event) {
        for (Album album : getSelectedAlbums().getAlbums()) {
            ViewLoader.showStage(album, "/view/AlbumView.fxml", album.getName(), new Stage());
        }
    }

    @FXML
    public void handleClose(ActionEvent event) {
        Platform.exit();
    }
}