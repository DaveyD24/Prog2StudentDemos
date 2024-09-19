
import java.util.Arrays;
import java.util.LinkedList;

public class App {
    public static void main(String[] args) {
        LinkedList<Animal> farm = new LinkedList<Animal>();
        farm.addAll(Arrays.asList(new Dog("Jack Russell"), new Cat("Calico"), new Frog()));
        for (Animal a : farm) {
            if (a instanceof Pettable) {
                ((Pettable) a).pet();
            }
        }
    }
}
