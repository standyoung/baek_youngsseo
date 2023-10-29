
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        double change = 0;

        for(int i=0;i<t;i++) {
            double num = sc.nextDouble();
            String unit = sc.next();
            if (unit.equals("kg")) {
                change = num * 2.2046;
                unit = "lb";
            }
            else if (unit.equals("lb")) {
                change = num * 0.4536;
                unit = "kg";
            }
            else if (unit.equals("l")) {
                change = num * 0.2642;
                unit = "g";
            }
            else if (unit.equals("g")) {
                change = num * 3.7854;
                unit = "l";
            }
            System.out.printf("%.4f %s\n",Math.round(change*1e4)/1e4,unit);
            // Math.round() : 소수점 n번째 자리까지 남고기자 할 때의 코드
            // n+1번째 자리에서 반올림
            // Math.round(e*m)/m
        }
    }
}

