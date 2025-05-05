import au.edu.uts.ap.javafx.ViewLoader;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.stage.Stage;
import model.Album;
import model.Albums;
import model.RecordStore;

import java.util.Arrays;

public class RecordStoreApp extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        ViewLoader.showStage(seededRecordStore(), "/view/RecordStoreView.fxml", "Record Store", new Stage());
    }

    private RecordStore seededRecordStore() {
        return new RecordStore(
                new Albums(FXCollections.observableArrayList(Arrays.asList(
                        new Album("TWICE", "Ready To Be", 12, 34.99, "/view/image/ready_to_be.jpg"),
                        new Album("WJSN", "As You Wish", 12, 34.99, "/view/image/as_you_wish.png"),
                        new Album("IVE", "Love Dive", 12, 29.99, "/view/image/love_dive.jpeg"))))
        );
    }
}
