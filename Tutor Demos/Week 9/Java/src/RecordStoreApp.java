import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class RecordStoreApp extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("RecordStoreView.fxml"));
        Parent root = fxmlLoader.load();
        stage.setScene(new Scene(root));
        stage.setTitle("Record Store");
        stage.show();
    }
}