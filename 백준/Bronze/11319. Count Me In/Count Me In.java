
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // nextInt() 마지막 개행문자 제거안해줌
        sc.nextLine();
        for (int i=0;i<t;i++) {
            String s = sc.nextLine();
            s = s.toLowerCase();
            int v_cnt = 0;
            int c_cnt = 0;
            
            for (int j=0;j<s.length();j++) {
                if (s.charAt(j)=='a' || s.charAt(j)=='e'||s.charAt(j)=='i'||s.charAt(j)=='o'||s.charAt(j)=='u'){
                    v_cnt += 1;
                }
                else if (s.charAt(j)!=' ') {
                    c_cnt += 1;
                }
            }
            System.out.println(c_cnt+" "+v_cnt);
        } //for testcase

    }
}

