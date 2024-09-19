public class Dog extends Animal implements Pettable{
    private String breed;

    public Dog(String breed) {
        super(100, AnimalType.MAMMAL);
        this.breed = breed;
    }

    @Override
    public void makeNoise() {
        System.out.println("Woof");
    }

    public void pet() {
        char choice;
        while ((choice = readChoice()) != 'x') {
            makeNoise();
        }
    }
}
