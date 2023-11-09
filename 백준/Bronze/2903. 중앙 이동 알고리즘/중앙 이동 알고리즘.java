
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int base = 0;

        /*
        1번 3^2 = (3+0)^2
        2번 5^2 = (3+2^1)^2
        3번 9^2 = (3+2^1+2^2)^2
        4번 17^2 = (3+2^1+2^2+2^3)^2
        */

        if (N == 1) {
            base = 3;
            System.out.println((int)Math.pow(base, 2));
        } else {
            for (int i = 1; i < N; i++) {
                base += Math.pow(2, i);
            }
            base += 3;
            System.out.println((int) Math.pow(base, 2));
        }
    }
}

