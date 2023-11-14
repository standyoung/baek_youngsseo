
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        double V_result = 0.0;

        for (int i=0;i<N;i++) {
            int A = sc.nextInt();
            double Apercent = A*0.01;
            V_result = 1-(1-V_result)*(1-Apercent);
            System.out.println(V_result*100);
        }
    }
}

