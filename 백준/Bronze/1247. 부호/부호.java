
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i=0;i<3;i++) {
            int t = sc.nextInt();
            BigInteger sum = new BigInteger("0");
            for (int j=0;j<t;j++) {
                BigInteger num = sc.nextBigInteger();
                sum = sum.add(num);
            }
            int compare = sum.compareTo(BigInteger.ZERO);
            if (compare==-1) {// 음수
                System.out.println("-");
            }
            else if (compare==0) {// 0
                System.out.println("0");
            }
            else if (compare==1) {// 양수
                System.out.println("+");
            }
        }
    }
}

