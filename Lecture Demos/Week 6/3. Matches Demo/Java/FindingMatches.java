import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

public class FindingMatches {
    public static void main(String[] args) {
        LinkedList<String> words = new LinkedList<String>(Arrays.asList("snooze", "david", "zed", "dyer"));
        
        System.out.println("List before: ");
        for (String word : words) { System.out.println(word); }
        
        removeZWords(words);
        
        System.out.println("List after: ");
        for (String word : words) { System.out.println(word); }
    }

    //Useful method for returning the matches themself
    // private static LinkedList<String> zWords(LinkedList<String> words) {
    //     LinkedList<String> matches = new LinkedList<String>();
    //     for (String word : words) {
    //         if (word.contains("z")) {
    //             matches.add(word);
    //         }
    //     }
    //     return matches;
    // }

    private static boolean isZWord(String word) {
        return word.contains("z");
    }

    private static void removeZWords(LinkedList<String> words) {
        LinkedList<String> wordsToRemove = new LinkedList<String>();
        for (String word : words) {
            if (isZWord(word)) {
                wordsToRemove.add(word);
            }
        }
        words.removeAll(wordsToRemove);
    }
}