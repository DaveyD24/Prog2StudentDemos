import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.text.DecimalFormat;

public class Seller extends Application {
    public static void main(String[] args) {
        launch(args);
    }

    private Label albumNameLbl;
    private TextField amountTf;
    private Button buyBtn;
    private Label profitLbl;
    private Text profitTxt;

    double SALE_PRICE = 34.99;

    @Override
    public void start(Stage stage) {

        albumNameLbl = new Label("Serenity");
        amountTf = new TextField("1");
        buyBtn = new Button("Buy");
        profitLbl = new Label("Profit: ");
        profitTxt = new Text("0");

        buyBtn.setOnAction(event -> sell());

        HBox hbox = new HBox(albumNameLbl, amountTf, buyBtn, profitLbl, profitTxt);
        hbox.setAlignment(Pos.CENTER);
        hbox.setSpacing(10);
        hbox.setPadding(new Insets(5));

        stage.setScene(new Scene(hbox));
        stage.setTitle("Seller");
        stage.show();
    }

    private int getAmount() {
        return Integer.parseInt(amountTf.getText());
    }

    private double getCurrentProfit() {
        return Double.parseDouble(profitTxt.getText());
    }

    private void sell() {
        double sale = getAmount() * SALE_PRICE;
        profitTxt.setText(formatted(sale+getCurrentProfit()));
    }

    private String formatted(double amount) {
        return new DecimalFormat(("#0.##")).format(amount);
    }
}