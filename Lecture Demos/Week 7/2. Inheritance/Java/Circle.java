public class Circle extends Shape{
    private double radius;

    public Circle(double radius) {
        super(1);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public int noCorners() {
        return 0;
    }
}


















// public class Circle extends Shape{
    
//     public Circle() {
//         super(1);
//     }

//     @Override
//     public String getAreaFormula() {
//         return "PI*r^2";
//     }

//     @Override
//     public String getPerimeterFormula() {
//         return "2*PI*r";
//     }

//     @Override
//     public int noCorners() {
//         return 0;
//     }
// }
