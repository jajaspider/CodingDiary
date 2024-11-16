import java.util.Scanner;

public class boj2579 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] Tlist = new int[T];
        for(int i=0;i<T;i+=1){
            Tlist[i] = sc.nextInt();
        }

        int[] Tlistsum = new int[T];
        Tlistsum[0]=Tlist[0];
        if (T > 1) {
            Tlistsum[1]=Tlist[0]+ Tlist[1];
        }
        if(T>2){
            Tlistsum[2]=Math.max(Tlist[0]+Tlist[2],Tlist[1]+Tlist[2]);
            for(int i=3;i<T;i+=1){
                Tlistsum[i]=Math.max(Tlist[i]+Tlistsum[i-2],Tlist[i]+Tlist[i-1]+Tlistsum[i-3]);
            }
        }
        System.out.println(Tlistsum[T-1]);
    }
}
