import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.*;

public class Incrementer extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    Label valueLbl;
    TextField valueTf;
    Button plusBtn;
    Button minusBtn;
    Button clearBtn;

    @Override
    public void start(Stage stage) {
        valueLbl = new Label("Value:");
        valueTf = new TextField("0");
        plusBtn = new Button("+");
        minusBtn = new Button("-");
        clearBtn = new Button("C");

        plusBtn.setOnAction(lambda -> setValue(getValue() + 1));
        minusBtn.setOnAction(lambda -> setValue(getValue() - 1));
        clearBtn.setOnAction(lambda -> setValue(0));

        HBox hbox = new HBox(10, valueLbl, valueTf, plusBtn, minusBtn, clearBtn);
        hbox.setAlignment(Pos.CENTER);

        stage.setScene(new Scene(hbox));
        stage.setTitle("Demo");
        stage.show();
    }

    public int getValue() {
        return Integer.parseInt(valueTf.getText());
    }

    public void setValue(int value) {
        valueTf.setText(String.valueOf(value));
    }
}