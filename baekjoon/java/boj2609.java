import java.util.Scanner;

public class boj2609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int gcda = a;
        int gcdb = b;
        while (gcdb != 0) {
            int r = gcda % gcdb;
            gcda = gcdb;
            gcdb = r;
        }
        System.out.print(gcda + " ");
        System.out.println(a * b / gcda);
    }
}