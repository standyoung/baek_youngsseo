
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();

        while (true) {

            String inpt = sc.next();

            if (inpt.equals("=")) {
                System.out.println(a);
                break;
            }
            else {
                int b = sc.nextInt();
                    if (inpt.equals("+")) {
                        a = a+b;
                    } else if (inpt.equals("-")) {
                        a = a-b;
                    } else if (inpt.equals("*")) {
                        a = a*b;
                    } else if (inpt.equals("/")) {
                        a = (int)a/b;
                    }
            }

        }

    }
}

