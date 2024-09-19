import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {
        
        LinkedList<Animal> farm = new LinkedList<Animal>();
        farm.add(new Dog());
        farm.add(new Cat());
        farm.add(new Monkey());
        for (Animal a : farm) {
            if (a instanceof Pettable) {
                ((Pettable) a).pet();
            }
        }
    }
}
