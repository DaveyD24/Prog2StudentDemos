public class Sentence {

    private final String sentence;

    public Sentence(String sentence) {
        this.sentence = sentence;
    }

    public void display() {
        System.out.println("--------------------------------");
        System.out.println(sentence + ":");
        System.out.println("Total words in sentence: " + wordCount());
        System.out.println("Number of z words in this sentence: " + zCount());
        System.out.println(isPascalCase() ? "Sentence Is In Pascal Case" : "sentence is not in pascal case");
        System.out.println("--------------------------------");
    }

    public int wordCount() {
        return sentence.split(" ").length;
    }

    private int zCount() {
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
            if (word.toLowerCase().charAt(i) == 'z') {
                return true;
            }
        }
        return false;
    }

    //Advanced feature
    public boolean isPascalCase() {
        for (String word : sentence.split(" ")) {
            if (Character.isLowerCase(word.charAt(0))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String[] sentences = {"David is zhe worst tutor ever", "The Big Brown Fox Did Some Stuff I Guess", "time to muzz", "Example sentence", "exampleZ SentenzeZ"};
        for (String sentence : sentences) {
            new Sentence(sentence).display();
        }
    }
}