package com.sonaapi;

import java.util.Scanner;

public class boj1002 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for(int i=0;i<T;i+=1){
            String tempstring = sc.nextLine();
            String[] stringsplit = tempstring.split(" ");
            int x1 = Integer.parseInt(stringsplit[0]);
            int y1 = Integer.parseInt(stringsplit[1]);
            int r1 = Integer.parseInt(stringsplit[2]);
            int x2 = Integer.parseInt(stringsplit[3]);
            int y2 = Integer.parseInt(stringsplit[4]);
            int r2 = Integer.parseInt(stringsplit[5]);
            double distance = Math.sqrt(Math.pow((x2-x1),2)+Math.pow((y2-y1),2));
            if(x1==x2 && y1==y2 && r1==r2){
                System.out.println("-1");
            }
            else if((x1==x2 && y1==y2) || (distance>r1+r2) || (distance < Math.abs(r1-r2))){
                System.out.println("0");
            }
            else if ((distance==r1+r2) || Math.abs(r1-r2)==distance){
                System.out.println("1");
            }
            else{
                System.out.println("2");
            }
        }
        sc.close();
    }
}
