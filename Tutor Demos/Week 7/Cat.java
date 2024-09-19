public class Cat extends Animal implements Pettable{
    private String breed;

    public Cat(String breed) {
        super(100, AnimalType.MAMMAL);
        this.breed = breed;
    }

    @Override
    public void makeNoise() {
        System.out.println("Meow");
    }

    public void pet() {
        char choice;
        while ((choice = readChoice()) != 'x') {
            makeNoise();
        }
    }
}
