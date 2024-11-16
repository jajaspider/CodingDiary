import java.util.Scanner;

public class boj6186 {
    static char[][] matrix;
    static char[][] visit;

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int count = 0;
    static int result = 0;

    public static void dfs(int x, int y, int R, int C) {
        visit[x][y] = '1';
        if (matrix[x][y] == '#') {
            count += 1;
        }
        int newX, newY;
        for (int i = 0; i < 4; i += 1) {
            newX = x + dx[i];
            newY = y + dy[i];

            if (0 <= newX && newX < R && 0 <= newY && newY < C && visit[newX][newY] == '0' && matrix[newX][newY]=='#') {
                dfs(newX, newY, R, C);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int R = sc.nextInt();
        int C = sc.nextInt();


        matrix = new char[R][C];
        visit = new char[R][C];
        for (int i = 0; i < R; i += 1) {
            String temp = sc.next();
            for (int j = 0; j < temp.length(); j += 1) {
                matrix[i][j] = temp.charAt(j);
                visit[i][j] = '0';
            }
        }

        for (int i = 0; i < R; i += 1) {
            for (int j = 0; j < C; j += 1) {
                count = 0;
                if (visit[i][j] != '1' && matrix[i][j]=='#') {
                    dfs(i, j, R, C);
                    if (count > 0) {
                        result += 1;
                    }
                }
            }
        }
        System.out.println(result);


//        for(int i=0;i<R;i+=1){
//            for(int j=0;j<C;j+=1){
//                System.out.print(matrix[i][j]);
//            }
//            System.out.printlen("");
//        }
    }
}
