package com.sonaapi;

import java.util.Scanner;

public class boj6591 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String T = sc.nextLine();
            String[] Tsplit = T.split(" ");
            if (Tsplit[0].equals("0") && Tsplit[1].equals("0")) {
                break;
            }
            int n = Math.min(Integer.parseInt(Tsplit[0]) - Integer.parseInt(Tsplit[1]), Integer.parseInt(Tsplit[1]));

            long temp = 1;
            for (int i = 0; i < n; i += 1) {
                temp *= (Integer.parseInt(Tsplit[0]) - i);
                temp /= (i+1);
            }
            System.out.println(temp);
        }
    }
}
