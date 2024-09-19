public class Cat extends Animal implements Pettable{
    public Cat() {
        super(4);
    }

    public void pet() {
        System.out.println("Petting cat...");
        happiness -= 0.1;
    }
}