package code;

public class MyQueueL_651514 {
    private Node head, tail;

    public MyQueueL_651514() {
        head = tail = null;
    }

    public void enqueue(String d) {
        Node n = new Node(d);
        if (head == null)
            head = tail = n;
        /* your code */
        else {
            tail.next = n;
            tail = n;
        }
    }

    public String dequeue() {
        if (isEmpty())
            return "";
        String value = head.value;
        head = head.next;
        /* your code */
        if (head == null)
            tail = null;
        return value;
    }

    /* isFull() isEmpty() */
    public boolean isEmpty() {
        return head == null;
    }

    public boolean isFull() {
        return false;
    }

    public String top() {
        return head.value;
    }

    public String getLast() {
        return tail.value;
    }

    public String dumpToString() {
        StringBuffer sb = new StringBuffer();
        Node n = head;
        while (n != null) {
            sb.append(n.value + " ");
            n = n.next;
        }
        return sb.toString();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("First->");
        Node temp = head;
        while (temp != null) {
            sb.append(
                    temp.value).append("->");
            temp = temp.next;
        }
        sb.append("Last");
        return sb.toString();
    }
}