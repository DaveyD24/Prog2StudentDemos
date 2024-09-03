import java.util.*;
import java.io.*;

public class In {
    private static Scanner scanner = new Scanner(System.in);

    static {
		try {
    	    File inputFile = new File("/home/Input.txt");
    	    if (inputFile.length() > 1) { 
    	        System.setIn(new FileInputStream(inputFile));
    	    }
    	    scanner = new Scanner(System.in);
    	} catch (FileNotFoundException e) {
    	    throw new RuntimeException(e);
    	}
	}

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