
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        int flag = 0;

        for (int i = 0; i < n; i++) {
            int score = sc.nextInt();
            if (score == 1) {
                flag += 1;
                sum += flag;
            }
            else if (score == 0) {
                flag = 0;
                sum += flag;
            }
        }
        
//        System.out.println(Arrays.toString(scArr));
        System.out.println(sum);
    }
}
