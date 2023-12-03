package code;

public class Node {
    String value;
    Node next;

    public Node(String d) {
        value = d;
        next = null;
    }

    public Node(String d, Node n) {
        value = d;
        next = n;
    }

    public String toString() {
        return value;
    }
}
