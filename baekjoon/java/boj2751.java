import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class boj2751 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = sc.nextInt();
        ArrayList<Integer> Nlist = new ArrayList<>();
        for (int i = 0; i < N; i += 1) {
            Nlist.add(sc.nextInt());
        }

        Collections.sort(Nlist);

        for (int i : Nlist) {
            sb.append(i).append('\n');
        }
        System.out.println(sb);
    }
}
