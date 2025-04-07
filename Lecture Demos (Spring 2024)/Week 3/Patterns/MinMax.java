//package Lecture.Patterns;

public class MinMax {
    public static void main(String[] args) {
        Min();
        Max();
    }

    public static void Min() {
        int[] nums = {1148, 1124, 1156, 1145, 1198, 1123, 1114, 1178, 1192};

        int min = Integer.MAX_VALUE;
        for (int num : nums) {
            if (num < min) {
                min = num;
            }
        }
        System.out.println("Smallest Value: " + min);
    }

    public static void Max() {
        int[] nums = {1148, 1124, 1156, 1145, 1198, 1123, 1114, 1178, 1192};

        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            if (num > max) {
                max = num;
            }
        }
        System.out.println("Smallest Value: " + max);
    }
}
