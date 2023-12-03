package code;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class Puzzle8_651514 {

    int size = 3;
    int[] sequence;
    public ArrayList<Puzzle8State> explored;
    Stack<Puzzle8State> dfs;

    public Puzzle8_651514(int[] sequence) {
        this.sequence = new int[size * size];
        int val = 0, index = 0;
        for (int i = 0; i < sequence.length; i++) {
            if (i % size == 0)
                val = sequence[i];
            else if (i % size == 1)
                index += sequence[i] * size;
            else {
                index += sequence[i];
                this.sequence[index] = val;
                index = 0;
            }
        }
        explored = new ArrayList<>();
        dfs = new Stack<>();
    }

    public void displayBoard() {
        for (int i = 0; i < size * size; i++) {
            if (i % size == 0)
                System.out.println();
            System.out.print(sequence[i] + " ");
        }
        System.out.println();
    }

    public void generateNextMove() {
        int blankPos = -1;
        for (int i = 0; i < sequence.length; i++) {
            if (sequence[i] == 9) {
                blankPos = i;
                break;
            }
        }

        if (blankPos == -1)
            return;

        if (blankPos + size < size * size) {
            swapAndPrintMove(blankPos, blankPos + size, "south");
        }
        if (blankPos - size > -1) {
            swapAndPrintMove(blankPos, blankPos - size, "north");
        }
        if (blankPos % size < size - 1) {
            swapAndPrintMove(blankPos, blankPos + 1, "east");
        }
        if (blankPos % size > 0) {
            swapAndPrintMove(blankPos, blankPos - 1, "west");
        }
    }

    private void swapAndPrintMove(int blankPos, int newPos, String direction) {
        this.sequence[newPos] = this.sequence[newPos] + this.sequence[blankPos];
        this.sequence[blankPos] = this.sequence[newPos] - this.sequence[blankPos];
        this.sequence[newPos] = this.sequence[newPos] - this.sequence[blankPos];

        Puzzle8State sequence_state = new Puzzle8State(Arrays.copyOf(this.sequence, this.sequence.length));
        if (!explored.contains(sequence_state)) {
            explored.add(sequence_state);
            dfs.push(new Puzzle8State(Arrays.copyOf(sequence_state.sequence, sequence_state.sequence.length)));
        }

        this.sequence[newPos] = this.sequence[newPos] + this.sequence[blankPos];
        this.sequence[blankPos] = this.sequence[newPos] - this.sequence[blankPos];
        this.sequence[newPos] = this.sequence[newPos] - this.sequence[blankPos];

        System.out.println("pushing " + direction + " " + Arrays.toString(this.sequence));
    }

    public void nextMoveWithStack() {
        Puzzle8State start = new Puzzle8State(Arrays.copyOf(this.sequence, this.sequence.length));
        dfs.push(start);
        // System.out.println(dfs);
        while (!dfs.isEmpty()) {
            this.sequence = dfs.pop().sequence;
            generateNextMove();
            if (isGoal(this.sequence)) {
                System.out.println("number of pop invocations = " + explored.size());
                System.out.println("stack size = " + dfs.size());
                System.out.println("explored size = " + explored.size());
                return;
            }
        }
    }

    private boolean isGoal(int[] seq) {
        Puzzle8State currentState = new Puzzle8State(seq);
        Puzzle8State goalState = new Puzzle8State(new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9 });
        return goalState.equals(currentState);
    }
}