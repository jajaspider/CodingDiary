package com.sonaapi;

import java.util.Scanner;

public class boj3943 {

    public static void main(String[] args) {
        // write your code here
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i+=1){
            int n = sc.nextInt();
            int max = n;
            if(n==1){
                System.out.println("1");
                continue;
            }
            while(n!=1) {
                n = (n%2==0)?n/2:n*3+1;
                if (n>max){
                    max=n;
                }
            }
            System.out.println(max);
        }
        sc.close();
    }
}

