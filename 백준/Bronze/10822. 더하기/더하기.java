
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] s = sc.next().split(",");
        int sum = 0;

        for (int i =0;i<s.length;i++) {
            sum += Integer.parseInt(s[i]);
        }
        System.out.println(sum);
    }
}
