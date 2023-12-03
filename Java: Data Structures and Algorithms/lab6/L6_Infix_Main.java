import code.MyQueueL_651514;
import code.MyRPN;
import code.MyShuntingYard_651514;

public class L6_Infix_Main {
    public static void main(String[] args) {
        demo1();
        String infixString = "( 4 + 2 ) / 3 * ( 8 - 5 )";
        // expect 4 2 + 3 / 8 5 - *
        if (args.length > 0)
        infixString = args[0];
        computeInfix(infixString);
    }

    private static void demo1() {
        System.out.println("-----MyQueueL Tester-----");
        MyQueueL_651514 queue = new MyQueueL_651514();
        queue.enqueue("1");
        queue.enqueue("3");
        queue.enqueue("5");
        queue.enqueue("7");
        System.out.println(queue.dumpToString());
        System.out.println("Top " + queue.top());
        System.out.println("Last " + queue.getLast());
        System.out.println("Dequeue " + queue.dequeue());
        System.out.println("Dequeue " + queue.dequeue());
        System.out.println("Dequeue " + queue.dequeue());
        System.out.println("Dequeue " + queue.dequeue());
        queue.enqueue("9");
        System.out.println(queue);
        System.out.println("----MyQueueL Test End----");
    }

    public static void computeInfix(String infixString) {
        String postfixString = MyShuntingYard_651514.infixToPostfix(infixString);
        double ans = MyRPN.computeRPN(postfixString);
        System.out.println(ans);
    }
}