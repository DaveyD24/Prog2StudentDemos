public abstract  class Animal {
    private float fluffiness;
    private AnimalType type;

    public Animal(float fluffiness, AnimalType type) {
        this.fluffiness = fluffiness;
        this.type = type;
    }

    public abstract void makeNoise();

    protected char readChoice() {
        System.out.print("Press any key to pet the " + this.getClass().getSimpleName() + ". Press x to stop");
        return In.nextChar();
    }
}
