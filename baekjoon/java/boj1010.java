package com.sonaapi;

import java.util.Scanner;

public class boj1010 {
    public static int combi(int n,int r){
        if(r==0||r==n){
            return 1;
        }
        else{
            return combi(n-1,r-1)+combi(n-1,r);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0;i<T;i+=1){
            int N = sc.nextInt();
            int M = sc.nextInt();
            if(N>M){
                System.out.println(combi(N,M));
            }
            else {
                System.out.println(combi(M, N));
            }
        }
    }
}
