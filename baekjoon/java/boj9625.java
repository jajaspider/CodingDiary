import java.util.Scanner;

public class boj9625 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int K = sc.nextInt();
        int[] As = new int[K+1];
        int[] Bs = new int[K+1];
        As[0] = 1;
        As[1] = 0;
        Bs[0] = 0;
        Bs[1] = 1;

        for(int i=2;i<K+1;i+=1){
            As[i]=As[i-2]+As[i-1];
            Bs[i]=Bs[i-2]+Bs[i-1];
        }
        System.out.println(As[K]+" "+Bs[K]);

    }
}
