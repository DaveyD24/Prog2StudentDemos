public abstract class Animal {
    private int noLegs;
    protected double happiness;

    public Animal(int noLegs) {
        this.noLegs = noLegs;
        happiness = 0.5;
    }

    @Override
    public String toString() {
        return this.getClass().getSimpleName() + " has " + noLegs + " legs";
    }
}
