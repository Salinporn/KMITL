package code;

public class MyStackL {
    private Node top;

    public MyStackL() {
        top = null;
    }

    public void push(String d) {
        Node n = new Node(d);
        n.next = top;
        top = n;
    }

    public String pop() {
        if (isEmpty())
            return "";
        String value = top.value;
        top = top.next;
        return value;
    }

    public String peek() {
        return top.value;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public boolean isFull() {
        return false;
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        Node n = top;
        while (n != null) {
            sb.append(n.value + " ");
            n = n.next;
        }
        return sb.toString();
    }
}
