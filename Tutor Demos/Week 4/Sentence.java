public class Sentence {

    private String sentence;

    public Sentence(String sentence) {
        this.sentence = sentence;
    }


    public static void main(String[] args) {
        String[] sentences = {"David is zhe worst tutor ever", "The Big Brown Fox Did Some Stuff I Guess", "hi bruzz yez sir"};
        for (String sentence : sentences) {
            // Sentence s = new Sentence(sentence);
            // s.showZCount();
            // System.out.println(s.isPascalCase() ? "Very Nice" : "not good");
        }
    }
}