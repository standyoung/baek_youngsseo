//어떻게 풀었는지 모르겟다
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextInt();
        double l = sc.nextDouble();
        int melody = 0;

        for (; ; ) {
            if (Math.ceil(melody / (a)) == l) {
                System.out.println(melody);
                break;
            } else {
                melody += 1;
            }
        }// for문 end
    }
}
