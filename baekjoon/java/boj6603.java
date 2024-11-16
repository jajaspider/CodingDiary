package com.sonaapi;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class boj6603 {

    public static void main(String[] args) {
        /*
        7 1 2 3 4 5 6 7
        8 1 2 3 5 8 13 21 34
        0
         */

        Scanner sc = new Scanner(System.in);

        while (true) {
            String k = sc.nextLine();
            if (k.equals("0")) {
                break;
            }
            String[] klist = k.split(" ");
            int n = Integer.parseInt(klist[0]);
            String[] arr = new String[n];
            String[] result = new String[n];
            for (int i = 0; i < n; i += 1) {
                for (int j = 1; j < n + 1; j += 1) {
                    arr[j - 1] = klist[j];
                }
            }
            /*
            for (int i = 0; i < arr.length; i += 1) {
                System.out.println(arr[i]);
            }

            */


        }
    }

    void combination(String[] arr, String[] result, boolean[] visited, int depth, int count) {
        if(depth==count){
            System.out.println(result);
        }
        visited[depth] = true;
        result[depth] = arr[depth];
        combination(arr, result, visited, depth+1, count);

    }
    /*
    static void comb(String[] arr, boolean[] visited, int depth, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }

        if (depth == n) {
            return;
        }

        visited[depth] = true;
        comb(arr, visited, depth + 1, n, r - 1);

        visited[depth] = false;
        comb(arr, visited, depth + 1, n, r);
    }
    */


}
