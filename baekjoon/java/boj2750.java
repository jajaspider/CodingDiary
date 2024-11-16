import java.util.Arrays;
import java.util.Scanner;

public class boj2750 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Nlist = new int[N];
        for(int i=0;i<N;i+=1){
            Nlist[i] = sc.nextInt();
        }

        Arrays.sort(Nlist);
        for(int i : Nlist){
            System.out.println(i);
        }
    }
}
