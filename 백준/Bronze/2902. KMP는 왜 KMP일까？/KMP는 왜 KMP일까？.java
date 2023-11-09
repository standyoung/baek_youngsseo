
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        System.out.printf("%s", s.charAt(0));
        for (int i=0;i<s.length();i++) {
            if (s.charAt(i)=='-') {
                System.out.printf("%s", s.charAt(i+1));
            }
        }
    }
}