package code;

public class SillyLuckyNumber {
    private String breed;
    private int luckyNumber;
    private int threeDigit; // 0 to 999
    public SillyLuckyNumber(String s) {
        breed = s;
        for (int i = 0; i < breed.length(); i++)
            luckyNumber += breed.charAt(i);
        threeDigit = luckyNumber % 1000;
    }
    // getters
    @Override
    public String toString() {
        return "<<"+ breed + " " + luckyNumber + " " + threeDigit+">>";
    }
    public void setBreed(String b) {
        breed = b;
    }

    public String getBreed() {
        return breed;
    }

    public int getLuckyNum() {
        return luckyNumber;
    }

    public int getThreeDigit() {
        return threeDigit;
    }

    public void setLuckyNumber(int luckyNumber) {
        this.luckyNumber = luckyNumber;
    }

    public void setThreeDigit(int threeDigit) {
        this.threeDigit = threeDigit;
    }
}
