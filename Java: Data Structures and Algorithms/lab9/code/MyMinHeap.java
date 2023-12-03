package code;

public class MyMinHeap {
    int MAX_SIZE = 6;
    int heap[] = new int[MAX_SIZE];
    int size = 0;

    private void swap(int i, int j) {
        int t = heap[i];
        heap[i] = heap[j];
        heap[j] = t;
    }

    public void insert(int d) {
        int p = size++;
        heap[p] = d;
        int parent = (p - 1) / 2;
        while ((p > 0) && (heap[p] < heap[parent])) {
            swap(p, parent);
            p = parent;
            parent = (p - 1) / 2;
        }
    }

    public int remove() {
        int d = heap[0];
        heap[0] = heap[--size];
        int p = 0;
        while (true) {
            int left = 2 * p + 1;
            if (left >= size) {
                break;
            }
            int right = 2 * p + 2;
            if (right == size) {
                if (heap[p] > heap[left]) {
                    swap(p, left);
                }
                break;
            } else {
                int q = heap[left] < heap[right] ? left : right;
                if (heap[p] > heap[q]) {
                    swap(p, q);
                } else {
                    break;
                }
                p = q;
            }
        }
        return d;
    }

    public int peek() {
        return heap[0];
    }

    public boolean isFull() {
        return size == MAX_SIZE;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public String toString() {
        String s = "";
        for (int i = 0; i < size; i++)
            s += heap[i] + " ";
        return s;
    }
}