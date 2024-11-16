package com.sonaapi;

import java.util.Scanner;

public class boj11654 {

    public static void main(String[] args) {
        // write your code here
        Scanner sc = new Scanner(System.in);
        String N = sc.next();
        byte[] n = N.getBytes();
        for(int i=0;i<N.length();i+=1){
            System.out.println(n[i]);
        }

        sc.close();
    }
}