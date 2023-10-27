
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numArr = new int[3];
        int gap = 0;
        int result = 0;

        for (int i=0;i<3;i++) {
            numArr[i] = sc.nextInt();
        }
//        1 4 10
        Arrays.sort(numArr);
//        System.out.println(Arrays.toString(numArr));
        if (2*(numArr[1]-numArr[0])==(numArr[2]-numArr[1])) {
            gap = numArr[1]-numArr[0];
            System.out.println(gap+numArr[1]);
        }
        else if ((numArr[1]-numArr[0])==(numArr[2]-numArr[1])) {
            gap = numArr[1]-numArr[0];
            System.out.println(gap+numArr[2]);
        }
        else if ((numArr[1]-numArr[0])==2*(numArr[2]-numArr[1])) {
            gap = numArr[2]-numArr[1];
            System.out.println(gap+numArr[0]);
        }
    }
}

