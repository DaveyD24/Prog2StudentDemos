public abstract class Shape {
    protected int noSides;

    public Shape(int noSides) {
        this.noSides = noSides;
    }

    public abstract double area();

    public int noCorners() {
        return noSides;
    }
}




















// public abstract class Shape {
//     private int noSides;

//     public Shape(int noSides) {
//         this.noSides = noSides;
//     }

//     public abstract String getAreaFormula();
//     public abstract String getPerimeterFormula();

//     public int noCorners() {
//         return noSides;
//     }
// }
