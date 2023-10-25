
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i=0;i<t;i++) {
            int n = sc.nextInt();
            int c_sum = 0;
            double score = 0.0;
            for (int j=0;j<n;j++) {
                int c = sc.nextInt();
                double g = sc.nextDouble();
                c_sum += c;
                score += c*g;
            }
            System.out.println(c_sum+" "+Math.round(score/c_sum*10)/10.0);
            // Math.round() : 소수점 n번째 자리까지 남고기자 할 때의 코드,
            // n+1번째 자리에서 반올림한다.
            // Math.round(e*m)/m
        }
        }
    }

