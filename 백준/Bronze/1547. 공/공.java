
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int[] arr = new int[] {1,2,3,4};
        int idx_x = 0;
        int idx_y = 0;

        for (int i=0;i<m;i++) {
            int x_ = sc.nextInt(); // 3
            int y_ = sc.nextInt(); // 1

            for (int j=0;j<4;j++) {
                if (arr[j]==x_) {
                    idx_x = j;
                }else if (arr[j]==y_) {
                    idx_y = j;
                }
            }
            int tmp = 0;

            tmp = arr[idx_x];
            arr[idx_x] = arr[idx_y];
            arr[idx_y] = tmp;
        }
        if (arr.length == 0) {
            System.out.println(-1);
        }
        else {
            System.out.println(arr[0]);
        }
    }
}

