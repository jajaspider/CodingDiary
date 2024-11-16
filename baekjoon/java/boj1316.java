import java.util.Arrays;
import java.util.Scanner;

public class boj1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count=0;
        for(int i=0;i<N+1;i+=1){
            boolean groud_word = false;
            String previous_word = "";
            String Nword_string = sc.nextLine();
            char[] Nword = Nword_string.toCharArray();
            for(int j=0;j<Nword.length;j+=1){
                if(previous_word.lastIndexOf(Nword[j])==-1){
                    previous_word+=Nword[j];
                    groud_word=true;
                    continue;
                }
                else if(previous_word.lastIndexOf(Nword[j])==previous_word.length()-1){
                    groud_word=true;
                }
                else {
                    groud_word=false;
                    break;
                }
            }
//            System.out.println(previous_word);
            if(groud_word){
                count+=1;
            }

        }
        System.out.println(count);
    }
}
