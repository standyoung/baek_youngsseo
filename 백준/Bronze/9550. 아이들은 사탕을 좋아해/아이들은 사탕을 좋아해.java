import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i=0;i<T;i++) {
            int N = sc.nextInt();
            int K = sc.nextInt();
            int cnt = 0;

            for (int j=0;j<N;j++) {
                int c = sc.nextInt();
                cnt += (int) c / K;
            }

            System.out.println(cnt);
        }
    }
}

