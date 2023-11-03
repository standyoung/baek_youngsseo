
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int i = 0;
        while (Math.pow(2, i) <= N) {
            if (Math.pow(2, i) == N) {
                System.out.println(1);
                break;
            }
            i += 1;
        }
        if (Math.pow(2, i) != N) {
            System.out.println(0);
        }
    }
}

