import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

import code.MyArrDemo;
import code.SillyLuckyNumber;

public class L8a_Main {
    public static void main(String[] args) {
        ex0();
        demo1();
        demo2();
        demo3();
        demo4();
        demo5();
    }

    static void ex0() {
        System.out.println("-ex0---");
        int[] arr = { 7, 3, 1, 9, 6, 8, 4, 2, 5 };
        System.out.println(Arrays.toString(arr));
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));
    }

    static void demo1() {
        System.out.println("-demo1---");
        SillyLuckyNumber[] arr = {
            new SillyLuckyNumber("Terrier"), new SillyLuckyNumber("Jack"),
            new SillyLuckyNumber("Pom"), new SillyLuckyNumber("Beagle")
        };
        System.out.println(Arrays.toString(arr));
        // Comparator<SillyLuckyNumber> engine = new Comparator<>() {
        //     @Override
        //     public int compare(SillyLuckyNumber o1, SillyLuckyNumber o2) {
        //         return Integer.compare(o1.getLuckyNum(), o2.getLuckyNum());
        //     }
        // };
        Comparator<SillyLuckyNumber> engine = (o1, o2) -> Integer.compare(o1.getLuckyNum(), o2.getLuckyNum()); // your code (sort by luckyNumber)
        Arrays.sort(arr, engine);
        System.out.println(Arrays.toString(arr));
    }

    static void demo2() {
        System.out.println("-demo2----");
        ArrayList<SillyLuckyNumber> list = new ArrayList<>( Arrays.asList(new SillyLuckyNumber("Terrier"), new SillyLuckyNumber("Jack"),new SillyLuckyNumber("Pom"), new SillyLuckyNumber("Beagle")));
        System.out.println(list);
        Collections.sort(/* your code */ list, (o1, o2) -> Integer.compare(o1.getLuckyNum(), o2.getLuckyNum()));
        System.out.println(list);
    }

    static void demo3() {
        System.out.println("-demo3----");
        ArrayList<SillyLuckyNumber> list = new ArrayList<>( Arrays.asList(new SillyLuckyNumber("Terrier"), new SillyLuckyNumber("Jack"),new SillyLuckyNumber("Pom"), new SillyLuckyNumber("Beagle")));
        System.out.println(list);
        list.sort(Comparator.comparing(SillyLuckyNumber::getLuckyNum));
        System.out.println(list);
        // demo shallow copy
        ArrayList<SillyLuckyNumber> anotherList = new ArrayList<>(list.subList(0, list.size()));
        anotherList.get(0).setBreed("newBreed"); //Terrier
        System.out.println(list); //notice how Terrier in list is also effected
    }

    static void demo4() {
        System.out.println("-demo4----");
        MyArrDemo<SillyLuckyNumber> arr = new MyArrDemo<>();
        arr.add(new SillyLuckyNumber("Terrier"));
        arr.add(new SillyLuckyNumber("Jack"));
        arr.add(new SillyLuckyNumber("Pom"));
        arr.add(new SillyLuckyNumber("Beagle"));
        System.out.println(arr);
        arr.swap(1,3);
        System.out.println(arr);
    }

    static void selectionSort(MyArrDemo<SillyLuckyNumber> arr) {
        for (int i = 0; i < arr.currentSize(); i++) {
            int min = i;
            for (int j = i + 1; j < arr.currentSize(); j++) {
                if (arr.get(j).getLuckyNum() < arr.get(min).getLuckyNum()) {
                    min = j;
                }
            }
            arr.swap(i, min);
        }
    }

    static void demo5() {
        System.out.println("-demo5----");
        MyArrDemo<SillyLuckyNumber> arr = new MyArrDemo<>();
        arr.add(new SillyLuckyNumber("Terrier"));
        arr.add(new SillyLuckyNumber("Jack"));
        arr.add(new SillyLuckyNumber("Pom"));
        arr.add(new SillyLuckyNumber("Beagle"));
        arr.add(new SillyLuckyNumber("Cocker Spaniel"));
        arr.add(new SillyLuckyNumber("Basenji"));
        System.out.println(arr);
        selectionSort(arr);
        System.out.println(arr);
    }
}
