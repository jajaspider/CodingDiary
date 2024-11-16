package com.sonaapi;

import java.util.Scanner;

public class boj3004 {

    public static void main(String[] args) {
        // write your code here
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int a = T/2;
        int b = T-a;
        System.out.println((a+1)*(b+1));
        sc.close();
    }
}

