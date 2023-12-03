package code;

import java.util.Stack;

public class MyLinkedList_651514 {
    public class Node {
        int data;
        Node next;
        public Node(int d) {
        data = d;
        }
    }
    Node head = null;

    public void add(int d) {
        Node p = new Node(d);
        p.next = head;
        head = p;
    }

    public void insert(int d) {
        Node q = new Node(d);
        if (head == null || head.data >= q.data) {
            q.next = head;
            head = q;
        } else {
            Node p = head;
            while (p.next != null && p.next.data < q.data) {
                p = p.next;
            }
            q.next = p.next;
            p.next = q;
        }
    }

    public int find(int d) {
        Node p = head;
        int i = 0;
        while (p!=null) {
            if (p.data == d) {
                return i;
            }
            p = p.next;
            i++;
        }
        return -1;
    }

    public void delete(int d) {
        Node t = new Node(0);
        t.next = head;
        Node p = t;
        while( (p.next!=null) && (p.next.data!=d) ) {
            p = p.next;
        }
        if(p.next!=null) {
            p.next = p.next.next;
        }
        head = t.next;
    }

    public void append(int d) {
        Node newNode = new Node(d);
        if (head == null) {
            head = newNode;
        } else {
            Node last = head;
            while (last.next != null) {
                last = last.next;
            }
            last.next = newNode;
        }
    }

    private int size() {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    public void add(int [] d) {
        for (int i = d.length - 1; i >= 0; i--) {
            add(d[i]);
        }
    }

    public void insert(int [] d) {
        for (int i = d.length - 1; i >= 0; i--) {
            insert(d[i]);
        }   
    }

    public void q1_rotate_clockwise(int k) {
        if (k > size()) {
            return;
        }
        Node current = head;
        for (int i = 0; i < k; i++) {
            current = current.next;
        }
        Node newHead = current.next;
        current.next = null;
        current = newHead;
        while (current.next != null) {
            current = current.next;
        }
        current.next = head;
        head = newHead;
    }

    public void q2_reverse() {
        Node prev = null;
        Node current = head;
        Node next = null;
        while (current != null) {
            next = current.next; // save next
            current.next = prev; // reverse
            prev = current; // move prev
            current = next; // move current
        }
        head = prev;
    }

    public void q3_remove_dup() {
        Node current = head;
        while (current != null) {
            Node runner = current;
            while (runner.next != null) {
                if (runner.next.data == current.data) {
                    runner.next = runner.next.next;
                } else {
                    runner = runner.next;
                }
            }
            current = current.next;
        }
    }

    public void q4_increment_digits() {
        q2_reverse();
        Node current = head;
        int carry = 1;
        while (current != null) {
            current.data += carry;
            if (current.data == 10) {
                current.data = 0;
                carry = 1;
            } else {
                carry = 0;
            }
            current = current.next;
        }
        if (carry == 1) {
            add(1);
        }
        q2_reverse();
    }

    public boolean q5_isPalindrome() {
        Node slow = head;
        Node fast = head;
        Stack<Integer> stack = new Stack<Integer>();
        while (fast != null && fast.next != null) {
            stack.push(slow.data);
            slow = slow.next;
            fast = fast.next.next;
        }
        if (fast != null) { // odd length
            slow = slow.next;
        }
        while (slow != null) {
            if (slow.data != stack.pop()) {
                return false;
            }
            slow = slow.next;
        }
        return true;
    }

    public String toString() {
        StringBuffer sb = new StringBuffer("head ");
        Node p = head;
        while(p!=null) {
            sb.append("--> [");
            sb.append(p.data);
            sb.append("] ");
            p = p.next;
        }
        sb.append("-> null");
        return new String(sb);
    }
}
