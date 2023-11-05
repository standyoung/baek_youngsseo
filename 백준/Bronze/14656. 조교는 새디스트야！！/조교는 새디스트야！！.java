
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int sum = 0;

        for (int i=1;i<N+1;i++) {
            int num = sc.nextInt();
            if (num!=i) {
                sum+=1;
            }
        }
        System.out.println(sum);
    }
}

