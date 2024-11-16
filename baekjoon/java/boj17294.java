import java.util.Scanner;

public class boj17294 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String k = sc.nextLine();
        if(k.length()==1 || k.length()==2) {
            System.out.println("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!");
            return;
        }
        int diff = 0;
        char[] Ks = k.toCharArray();
        for(int i=0;i<k.length()-1;i+=1){
            if(i==0){
                diff=Ks[i]-Ks[i+1];
            }
            if(diff != (Ks[i]-Ks[i+1])){
                System.out.println("흥칫뿡!! <(￣ ﹌ ￣)>");
                return;
            }
        }
        System.out.println("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!");
    }
}
