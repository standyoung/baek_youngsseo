
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strArray = sc.next().split(",");
        int cnt = 0;

        for (String s:strArray) {
            cnt += 1;
        }
        
        System.out.println(cnt);
    }
}

