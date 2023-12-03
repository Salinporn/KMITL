package code;

public class MyArray_65011514 extends MyArrayBasic_65011514 {
    public MyArray_65011514() {
        MAX_SIZE = 100_000;
        data = new int[MAX_SIZE];
    }

    public MyArray_65011514(int max) {
        MAX_SIZE = max;
        data = new int[MAX_SIZE];
    }

    public boolean isFull() {
        return size == MAX_SIZE;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    private int[] expandByK(int k) {
        MAX_SIZE *= k;
        int newData[] = new int[MAX_SIZE];
        System.arraycopy(data, 0, newData, 0, size);
        return newData;
    }

    private int[] expand() {
        return expandByK(2);
    }

    @Override
    public void add(int d) {
        if (isFull()) {
            data = expand();
        }
        super.add(d);
    }

    @Override
    public void delete(int index){
        if (!isEmpty()) {
            super.delete(index);
        }
    }
}
