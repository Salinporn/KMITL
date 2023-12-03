package code;

public class MyStackA {
    int MAX_SIZE=100;
    double stack[] = new double[MAX_SIZE];
    int top = 0;

    void push(double d) {
        if(top == MAX_SIZE) {
            System.out.println("Stack overflow");
            return;
        }
        stack[top++] = d;
    }

    double pop() {
        if(top == 0) {
            System.out.println("Stack underflow");
            return 0;
        }
        return stack[--top];
    }

    double top() {
        if(top == 0) {
            System.out.println("Stack underflow");
            return 0;
        }
        return stack[top-1];
    }

    boolean isFull() {
        return top == MAX_SIZE;
    }

    boolean isEmpty() {
        return top == 0;
    }

    public String toString() {
        StringBuffer sb = new StringBuffer();
        sb.append("top->");
        for(int i=top-1; i>=0; i--) {
            sb.append("[");
            sb.append(stack[i]);
            sb.append("]->");
        }
        sb.append("bottom");
        return new String(sb);
    }
}