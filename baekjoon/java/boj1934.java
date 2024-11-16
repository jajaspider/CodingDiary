import java.util.Scanner;

public class boj1934 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i += 1) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int gcda = a;
            int gcdb = b;
            while (gcdb != 0) {
                int r = gcda % gcdb;
                gcda = gcdb;
                gcdb = r;
            }
            System.out.println(a * b / gcda);
        }
    }
}