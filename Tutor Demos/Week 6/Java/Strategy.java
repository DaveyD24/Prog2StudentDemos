enum Focus {
    Attack,
    Defence
}

public class Strategy {
    private Focus focus;
    public Strategy() {
        this.focus = Focus.Attack;
    }

    public void changeStrategy() {
        focus = (focus == Focus.Attack) ? Focus.Defence : Focus.Attack;
        System.out.println("Strategy changed to " + focus);
    }

    @Override
    public String toString() {
        return this.focus.toString();
    }
}
