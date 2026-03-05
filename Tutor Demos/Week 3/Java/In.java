import java.util.*;
import java.io.*;

public class In {
    private static Scanner scanner = new Scanner(System.in);

    public static String nextLine() {
        return scanner.nextLine();
    }

    public static char nextChar() {
        return scanner.nextLine().charAt(0);
    }

    public static int nextInt() {
        int value = scanner.nextInt();
        scanner.nextLine();
        return value;
    }

    public static double nextDouble() {
        double value = scanner.nextDouble();
        scanner.nextLine();
        return value;
    }
}