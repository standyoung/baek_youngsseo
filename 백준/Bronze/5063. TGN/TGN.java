
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();


        for (int i=0;i<N;i++) {
            int r = sc.nextInt();
            int e = sc.nextInt();
            int c = sc.nextInt();

            int sum = 0;
            sum = e-c;

            if (r<(e-c)) {
                System.out.println("advertise");
            } else if (r>(e-c)) {
                System.out.println("do not advertise");
            } else {
                System.out.println("does not matter");
            }

        }
    }
}

