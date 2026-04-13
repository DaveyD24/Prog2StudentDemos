import au.edu.uts.ap.javafx.ViewLoader;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.stage.Stage;
import model.Album;
import model.Albums;
import model.RecordStore;

import java.util.Arrays;

public class App extends Application {
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
                        new Album("Stardust", "Serenity", 12, 34.99),
                        new Album("Takio Senzu", "Oceans", 12, 34.99),
                        new Album("Haru Yelin", "Alive", 12, 29.99),
                        new Album("Stardust", "Chords", 12, 29.99),
                        new Album("Rin Kadoshi", "Lost", 12, 29.99),
                        new Album("Haru Yelin", "Wind", 12, 29.99)
                )))
        );
    }
}