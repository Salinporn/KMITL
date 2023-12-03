package code;
import java.util.regex.Pattern;

public class MyRPN {
    private static Pattern pattern = Pattern.compile("-?\\d+(\\.\\d+)?");
    public static boolean isNumeric(String strNum) {
        if (strNum == null)
        return false;
        return pattern.matcher(strNum).matches();
    }
    public static double computeRPN(String rpn) {
        MyStackA stack = new MyStackA();
        String[] tokens = rpn.split(" ");
        for (String token : tokens) {
            if (isNumeric(token)) {
                stack.push(Double.parseDouble(token));
            } else {
                double op2 = stack.pop();
                double op1 = stack.pop();
                switch (token) {
                    case "+":
                        stack.push(op1 + op2);
                        break;
                    case "-":
                        stack.push(op1 - op2);
                        break;
                    case "*":
                        stack.push(op1 * op2);
                        break;
                    case "/":
                        stack.push(op1 / op2);
                        break;
                    default:
                        System.out.println("Invalid operator");
                        break;
                }
            }
        }
        return stack.pop();
    }
}