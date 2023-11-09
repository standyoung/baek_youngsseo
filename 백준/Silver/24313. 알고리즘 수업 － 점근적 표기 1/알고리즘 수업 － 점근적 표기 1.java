
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a1 = sc.nextInt();
        int a0 = sc.nextInt(); // f(n) = 7n+7, f(1) = 14
        int c = sc.nextInt(); // c = 8, c*g(1) = 8
        int n0 = sc.nextInt(); // O(g(n)) = n

        // f(n0) <= c*n0
        if ((a1*n0+a0) <= c*n0 && a1<=c) {
            // (a1 - c) n + a0 <= 0에서
            // a1<=c
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}

