package com.sonaapi;

import java.util.Scanner;

public class boj2864 {

    public static void main(String[] args) {
        char[] tempArray1;
        Scanner sc = new Scanner(System.in);

        String AB = sc.nextLine();
        String[] ABSplit = AB.split(" ");
        String A = ABSplit[0];
        String B = ABSplit[1];

        tempArray1 = A.toCharArray();
        for(int i=0;i< tempArray1.length;i+=1){
            if(tempArray1[i] =='6'){
                tempArray1[i] ='5';
            }
        }
        A = String.valueOf(tempArray1);

        tempArray1 = B.toCharArray();
        for(int i=0;i< tempArray1.length;i+=1){
            if(tempArray1[i] =='6'){
                tempArray1[i] ='5';
            }
        }
        B = String.valueOf(tempArray1);
        System.out.print(Integer.parseInt(A)+Integer.parseInt(B)+" ");

        tempArray1 = A.toCharArray();
        for(int i=0;i< tempArray1.length;i+=1){
            if(tempArray1[i] =='5'){
                tempArray1[i] ='6';
            }
        }
        A = String.valueOf(tempArray1);
        tempArray1 = B.toCharArray();
        for(int i=0;i< tempArray1.length;i+=1){
            if(tempArray1[i] =='5'){
                tempArray1[i] ='6';
            }
        }
        B = String.valueOf(tempArray1);
        System.out.println(Integer.parseInt(A)+Integer.parseInt(B));

        sc.close();
    }
}

