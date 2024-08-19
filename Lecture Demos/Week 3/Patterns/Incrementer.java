//package Lecture.Patterns;

public class Incrementer {
    public static void main(String[] args) {
        int x = 1;
        for (int i = 0; i < 10; i++) {
            System.out.println("Successfully incremented to " + (++x) + "...");
        }
    }
}