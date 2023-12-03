package code;

public class Puzzle8State {
    // int score;
    public int[] sequence;

    public Puzzle8State(int[] sequence) {
        this.sequence = sequence;
    }

    public int[] getSequence() {
        return sequence;
    }

    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        Puzzle8State other = (Puzzle8State) obj;
        for (int i = 0; i < sequence.length; i++) {
            if (this.sequence[i] != other.sequence[i]) {
                return false;
            }
        }
        return true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < sequence.length; i++) {
            sb.append(sequence[i]).append(" ");
            if ((i + 1) % 3 == 0) {
                sb.append("\n");
            }
        }
        return sb.toString();
    }
}