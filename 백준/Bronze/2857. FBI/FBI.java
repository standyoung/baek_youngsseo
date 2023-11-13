
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        /*참고코드*/
        Scanner sc = new Scanner(System.in);
        String[] code = new String[5];
        ArrayList<Integer> lst = new ArrayList<>();

        for (int i =0;i<5;i++) {
            code[i] = sc.next();
            if (code[i].contains("FBI")) {
                lst.add(i+1);
            }
        }
        if (lst.isEmpty()) {
            System.out.println("HE GOT AWAY!");
        }
        else {
            for (Object i : lst) {
                System.out.printf("%d ", i);
            }
        }



    }
}

