// public class Program {
//     public static void main(String[] args) {
//         int[] marks = {87, 76, 75, 85, 60, 51, 49, 50, 89, 100, 94, 82, 80, 91, 67};

//         //Compute sum (Sum pattern)
//         int sum = 0;
//         for (int mark : marks) {
//             sum += mark;
//         }

//         //Compute average
//         double average = (double)sum / marks.length;
        
//         //Print results
//         System.out.println("Average Mark: " + average);
//         System.out.println(isAllPassing(marks) ? "100% Pass Rate" : "Below 100% Pass Rate");
//         System.out.println(anyHighAcheivers(marks) ? "Someone Achieved 100" : "No High Achievers");
//     }

//     //Every pattern
//     private static boolean isAllPassing(int[] marks) {
//         for (int mark : marks) {
//             if (mark < 50) {
//                 return false;
//             }
//         }
//         return true;
//     }

//     //Any pattern
//     private static boolean anyHighAcheivers(int[] marks) {
//         for (int mark : marks) {
//             if (mark == 100) {
//                 return true;
//             }
//         }
//         return false;
//     }
// }