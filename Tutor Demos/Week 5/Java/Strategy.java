public class Strategy {
    private String focus;
    public Strategy() {
        this.focus = "Attack";
    }

    public void changeStrategy() {
        if (focus.equals("Attack")) {
            focus = "Defence";
        }
        else {
            focus = "Attack";
        }
        System.out.println("Strategy changed to " + focus);
    }

    @Override
    public String toString() {
        return this.focus;
    }
}
