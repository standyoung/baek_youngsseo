
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long max1 = 0;
        long max2 = 0;

        for (int i =0;i<N;i++) {
            long num = sc.nextLong();
            if (num>max1) {
                max1 = num;
            }
        }
        for (int i =0;i<M;i++) {
            long num = sc.nextLong();
            if (num>max2) {
                max2 = num;
            }
        }

        System.out.println(max1+max2);

    }
}

