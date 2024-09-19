public class Rectangle extends Shape{
    private double height;
    private double width;

    public Rectangle(int height, int width) {
        super(4);
        this.height = height;
        this.width = width;
    }

    @Override
    public double area() {
        return height * width;
    }
}













// public class Rectangle extends Shape{
    
//     private double height;
//     private double width;

//     public Rectangle() {
//         super(4);
//     }

//     @Override
//     public String getAreaFormula() {
//         return "h*w";
//     }

//     @Override
//     public String getPerimeterFormula() {
//         return "2(h+w)";
//     }
// }
