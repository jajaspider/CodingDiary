package com.sonaapi;

import java.util.Scanner;

public class boj5211 {
    public static void main(String[] args) {
        char[] tempArray1;
        Scanner sc = new Scanner(System.in);
        String N = sc.next();
        String N2 = N.replaceAll("|","");

        tempArray1 = N2.toCharArray();
        int Aminor = 0;
        int Cmajor = 0;

        for(int i=0;i< tempArray1.length;i+=1){
            if(tempArray1[i] =='C' || tempArray1[i] =='F' || tempArray1[i] =='G'){
                Cmajor+=1;
            }
            else if(tempArray1[i] =='A' || tempArray1[i] =='D' || tempArray1[i] =='E'){
                Aminor+=1;
            }
        }
        if(Cmajor==Aminor){
            if(tempArray1[tempArray1.length-1] =='C' || tempArray1[tempArray1.length-1] =='F' || tempArray1[tempArray1.length-1] =='G'){
                System.out.println("C-major");
            }
            else if(tempArray1[tempArray1.length-1] =='A' || tempArray1[tempArray1.length-1] =='D' || tempArray1[tempArray1.length-1] =='E'){
                System.out.println("A-minor");
            }
        }

        else if (Cmajor>Aminor){
            System.out.println("C-major");
        }
        else {
            System.out.println("A-minor");
        }

    }

}
