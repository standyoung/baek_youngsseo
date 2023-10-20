
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();
        int p = sc.nextInt();
        int y = 0;

        int x = a * p;

        if (p>=c) {
            y = b + (p-c)*d;
        }
        else {
            y = b;
        }

        if (x>=y) {
            System.out.println(y);
        }
        else if (x<y) {
            System.out.println(x);
        }
    }
}
