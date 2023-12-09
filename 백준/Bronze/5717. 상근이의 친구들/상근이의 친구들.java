
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int cnt = 0;

            int m = sc.nextInt();
            int f = sc.nextInt();

            if (m==0 && f==0) {
                break;
            }
            else {
                cnt = m+f;
                System.out.println(cnt);
            }
        }

    }
}

