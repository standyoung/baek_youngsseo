
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int V = sc.nextInt();
        String s = sc.next();

        int a_sum = 0;
        int b_sum = 0;

        for (int i=0;i<s.length();i++) {
            if (s.charAt(i)=='A') {
                a_sum += 1;
            }else if (s.charAt(i)=='B') {
                b_sum += 1;
            }
        }
        if (a_sum>b_sum) {
            System.out.println("A");
        } else if (a_sum<b_sum) {
            System.out.println("B");
        } else {
            System.out.println("Tie");
        }

    }
}

