
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int idx = 0;

        for (int i=0;i<5;i++) {
            int sum = 0;
            for (int j=0;j<4;j++) {
                int score = sc.nextInt();
                sum += score;
                if (sum>max) {
                    max = sum;
                    idx = i;
                }
            }
        }
        System.out.printf("%d %d",idx+1, max);
    }
}

