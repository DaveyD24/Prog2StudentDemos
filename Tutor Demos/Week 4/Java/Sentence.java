//Goal: Display each sentence in this form:
// - Sentence
// - Number of words: <n>
// - Number of z words: <n>
//
// z count should be case-insensitive

public class Sentence {

    private final String sentence;

    public Sentence(String sentence) {
        this.sentence = sentence;
    }

    public void display() {
        System.out.println("-----------------------");
        System.out.println(sentence);
        System.out.println("-----------------------");
        System.out.println("Number of words: " + wordCount());
        System.out.println("Number of z words: " + zWordCount());
    }

    private int wordCount() {
        String[] words = sentence.split(" ");
        return words.length;
    }

    private int zWordCount() {
        int count = 0;
        for (String word : sentence.split(" ")) {
            if (containsZ(word)) {
                count++;
            }
        }
        return count;
    }

    private boolean containsZ(String word) {
        for (int i = 0; i < word.length(); i++) {
            char c = word.toLowerCase().charAt(i);
            if (c == 'z') {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String[] sentences = {"David is zhe best tutor ever", "The Big Brown Fox Did Some Stuff I Guess", "time to muzz", "Example sentence", "exampleZ SentenzeZ"};
        for (String sentence : sentences) {
            Sentence s = new Sentence(sentence);
            s.display();
        }
    }
}