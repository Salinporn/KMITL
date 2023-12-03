package code;

import java.util.Arrays;

public class MyArrayBasic_65011514 {
    protected int MAX_SIZE = 5;
    protected int data[] = new int[MAX_SIZE];
    protected int size = 0;

    public void add(int d) {
        data[size] = d;
        size++;
    }

    public void insert(int d, int index) {
        for (int i = size; i > index; i--) {
            data[i] = data[i - 1];
        }
        data[index] = d;
        size++;
    }

    public int find(int d) {
        for (int i = 0; i < size; i++) {
            if (data[i] == d) {
                return i;
            }
        }
        return -1;
    }

    public int binarySearch(int d) {
        int left = 0;
        int right = size - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (data[mid] == d) {
                return mid;
            } else if (data[mid] < d) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1; // not found
    }

    public void delete(int index) {
        for (int i = index; i < size - 1; i++) {
            data[i] = data[i + 1];
        }
        size--;
    }

    public MyArrayBasic_65011514(int... a) {
        if (a != null) {
            for (int i = 0; i < a.length; i++) {
                if (i < MAX_SIZE){
                    add(a[i]);
                }
            }
        }
    }

    @Override
    public String toString() {
        return "MyArrayBasic [MAX_SIZE=" + MAX_SIZE + ", data=" + Arrays.toString(data) + ", size=" + size + "]";
    }
}