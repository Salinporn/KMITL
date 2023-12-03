package code;
import java.util.regex.Pattern;
import java.util.StringTokenizer;

public class MyRPN {
    public static double computeRPN(String postfixString) {
        MyStackL stack = new MyStackL();
        StringTokenizer st = new StringTokenizer(postfixString);
        while (st.hasMoreTokens()) {
            String t = st.nextToken();
            if (isNumeric(t))
                stack.push(t);
            else {
                double a = Double.parseDouble(stack.pop());
                double b = Double.parseDouble(stack.pop());
                double c = 0;
                switch (t) {
                    case "+":
                        c = b + a;
                        break;
                    case "-":
                        c = b - a;
                        break;
                    case "*":
                        c = b * a;
                        break;
                    case "/":
                        c = b / a;
                        break;
                }
                stack.push(String.valueOf(c));
            }
        }
        return Double.parseDouble(stack.pop());
    }

    public static boolean isNumeric(String str) {
        Pattern pattern = Pattern.compile("-?[0-9]+(\\.[0-9]+)?");
        return pattern.matcher(str).matches();
    }
}
