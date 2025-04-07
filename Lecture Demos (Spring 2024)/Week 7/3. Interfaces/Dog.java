public class Dog extends Animal implements Pettable{
    public Dog() {
        super(4);
    }

    public void pet() {
        System.out.println("Petting dog...");
        happiness += 0.2;
    }
}