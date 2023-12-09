
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1, n2, n3, n4 = 0;
        int i = 1;
        while (true) {
            int n0 = sc.nextInt();
            if (n0 == 0) {
                break;
            } else {
                n1 = 3 * n0;
                if ((n1 % 2) == 0) {
                    n2 = n1 / 2;
                } else {
                    n2 = (n1 + 1) / 2;
                } // n2

                n3 = 3 * n2; // n3
                n4 = (n3 / 9);

                if ((n1 % 2) == 0) {
                    System.out.println(i + ". " + "even " + n4);
                } else if ((n1 % 2) != 0) {
                    System.out.println(i + ". " + "odd " + n4);
                }
                i += 1;
            }
        }//while
    }
}

