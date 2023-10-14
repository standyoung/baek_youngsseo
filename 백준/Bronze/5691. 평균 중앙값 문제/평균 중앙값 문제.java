
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (; ; ) {

            int a = sc.nextInt();
            int b = sc.nextInt();

            if (a == 0 && b == 0) break;

            System.out.println(a - (b - a));
            // c가 제일 작은 정수
            // 오름차순으로 정렬했을 때 c a<=b
        }
    }
}
