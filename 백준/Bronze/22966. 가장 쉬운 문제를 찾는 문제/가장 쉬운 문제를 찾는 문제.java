
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int min = 5;
        String result = "";
        for (int i=0;i<n;i++) {
            String s = sc.next();
            int level = sc.nextInt();

            if (level<min) {
                min = level;
                result = s;
            }
        }
        System.out.println(result);
    }
}

