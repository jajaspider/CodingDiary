package com.sonaapi;

import java.util.Scanner;

public class boj1009 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = Integer.parseInt(sc.nextLine());
        for(int i=0;i<T;i+=1){
            int temp = 1;
            int a = sc.nextInt();
            int b = sc.nextInt();
            for(int j=0;j<b;j+=1) {
                temp = temp*a%10;
            }
            if (temp==0){
                temp=10;
            }
            System.out.println(temp);
        }
    }
}
