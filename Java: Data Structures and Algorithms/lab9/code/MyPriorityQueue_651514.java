package code;

public class MyPriorityQueue_651514 implements MyQueueInterface {
    private MyMinHeap minHeap = new MyMinHeap();

    @Override
    public void enqueue(int d) {
        if (!isFull()) {
            minHeap.insert(d);
        } else {
            System.out.println("Queue is full. Cannot enqueue " + d);
        }
    }

    @Override
    public int dequeue() {
        if (!isEmpty()) {
            return minHeap.remove();
        } else {
            System.out.println("Queue is empty. Cannot dequeue.");
            return -1;
        }
    }

    @Override
    public int front() {
        if (!isEmpty()) {
            return minHeap.peek();
        } else {
            System.out.println("Queue is empty. No front element.");
            return -1;
        }
    }

    @Override
    public boolean isFull() {
        return minHeap.isFull();
    }

    @Override
    public boolean isEmpty() {
        return minHeap.isEmpty();
    }

    public String toString() {
        return minHeap.toString();
    }
}