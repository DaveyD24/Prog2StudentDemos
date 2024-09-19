public class Frog extends Animal{

    public Frog() {
        super(0, AnimalType.AMPHIBIAN);
    }

    @Override
    public void makeNoise() {
        System.out.println("Ribbit");
    }
}
