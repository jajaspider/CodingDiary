package com.sonaapi;

import java.util.Scanner;

public class boj9012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int i = 0; i < T; i += 1) {
            String s = sc.next();
            char[] temp = s.toCharArray();
            int leftbracket = 0;
            int rightbracket = 0;

            for (char temp1 : temp) {
                if (temp1 == '(') {
                    leftbracket += 1;
                } else if (temp1 == ')') {
                    if (leftbracket > rightbracket) {
                        rightbracket += 1;
                    } else {
                        leftbracket = 0;
                        rightbracket = 1;
                        break;
                    }
                }
            }
            if (leftbracket == rightbracket) {
                System.out.println("YES");
                leftbracket = 0;
                rightbracket = 0;
                continue;
            } else {
                System.out.println("NO");
                leftbracket = 0;
                rightbracket = 0;
                continue;
            }
        }
    }
}
