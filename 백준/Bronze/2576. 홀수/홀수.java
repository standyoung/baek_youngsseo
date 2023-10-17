
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hap = 0;
        int min = 100;

        for (int i = 0; i < 7; i++) {
            int n = sc.nextInt();

            if ((n % 2) == 1) {
                hap += n;
                min = Math.min(min,n);
            }
        } // for문 end

        if (hap == 0) {
            System.out.println(-1);
        } else {
            System.out.println(hap);
            System.out.println(min);
//            System.out.println(Arrays.toString(arr)); // int형 배열 모두 출력
        }
    }
}
