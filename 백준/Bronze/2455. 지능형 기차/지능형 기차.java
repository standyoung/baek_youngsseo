
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int curr = 0;
        int max = 0;

        for (int i = 0; i < 4; i++) {
            int getoffT = sc.nextInt();
            int takeT = sc.nextInt();

            curr += takeT;
            curr -= getoffT;

            if (curr > max) {
                max = curr;
            }

        } //for문 end
        System.out.println(max);
        
    }
}
