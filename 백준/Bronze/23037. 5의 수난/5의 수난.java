
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int cnt = 0;
        for (int i=0;i<s.length();i++) {
             cnt += Math.pow(Integer.parseInt(String.valueOf(s.charAt(i))),5);
        }
        System.out.println(cnt);
    }
}

