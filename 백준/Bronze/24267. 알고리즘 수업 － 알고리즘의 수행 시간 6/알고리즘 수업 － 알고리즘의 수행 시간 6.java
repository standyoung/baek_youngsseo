
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1부터 n까지 중 3개 뽑기(i,j,k)
        long n = sc.nextLong();
        
        System.out.println((int)(n-2)*(n-1)*n/6);
        System.out.println(3);
    }
}

