import java.util.Scanner;

public class boj2847 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] Nlist = new int[N];
        for(int i=0;i<N;i+=1){
            Nlist[i] = sc.nextInt();
        }
        int count =0;
        if(Nlist.length>1){
            for(int i=Nlist.length-2;i>=0;i-=1){
                if(Nlist[i]>=Nlist[i+1]){
                    count+=(Nlist[i]-Nlist[i+1]+1);
                    Nlist[i] = Nlist[i+1]-1;
                }
            }
        }
        System.out.println(count);
    }
}
