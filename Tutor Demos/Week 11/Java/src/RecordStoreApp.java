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
                        new Album("Mayumi", "Serenity", 12, 34.99, "/view/image/Serenity.png"),
                        new Album("Takio Senzu", "Oceans", 12, 34.99, "/view/image/Oceans.png"),
                        new Album("Haru Yelin", "Alive", 12, 29.99, "/view/image/Alive.png"),
                        new Album("Mayumi", "Arblard", 12, 29.99, "/view/image/Arblard.png"),
                        new Album("Rin Kadoshi", "Lost", 12, 29.99, "/view/image/Lost.png")
        ))));
    }
}
