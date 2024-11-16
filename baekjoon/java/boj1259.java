package com.sonaapi;

import java.util.*;

public class boj1259 {
    public static String reverseString(String s) {
        return ( new StringBuffer(s) ).reverse().toString();
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        while(true){
            String pd = sc.nextLine();
            if(pd.equals("0")){
                break;
            }
            int pd_len = pd.length();
            if(pd_len%2==0){
                String temp1,temp2;
                temp1 = pd.substring(0,(pd_len/2));
                temp2 = pd.substring((pd_len/2),pd_len);
                String re_temp2 = reverseString(temp2);

                if(temp1.equals(re_temp2)){
                    System.out.println("yes");
                    continue;
                }
            }
            else {
                String temp1,temp2;
                temp1 = pd.substring(0,(pd_len/2));
                temp2 = pd.substring((pd_len/2)+1,pd_len);
                String re_temp2 = reverseString(temp2);

                if(temp1.equals(re_temp2)){
                    System.out.println("yes");
                    continue;
                }
            }
            System.out.println("no");
        }
    }
}

