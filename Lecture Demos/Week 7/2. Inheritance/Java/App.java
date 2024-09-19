import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {

        LinkedList<Shape> shapes = new LinkedList<Shape>();
        shapes.add(new Rectangle(4, 5));
        shapes.add(new Circle(4));
        for (Shape s : shapes) {
            System.out.println("Number of corners of my " + s.getClass().getSimpleName() + ": " + s.noCorners());
        }
    }
}
