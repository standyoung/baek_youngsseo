
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        int sum = 10;
        int plate = 0;

        for (int i=1;i<s.length();i++) {
            if (s.charAt(i-1)==s.charAt(i)) {
                plate = 5 ;
                }
            else {
                plate = 10;
            }
            sum += plate;
        }
        System.out.println(sum);
    }
}

