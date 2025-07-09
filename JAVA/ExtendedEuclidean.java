

import java.util.Scanner;

public class ExtendedEuclidean {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Please Enter values of M and N : ");
        int m = sc.nextInt();
        int n = sc.nextInt();
        int s, s1 = 1, s2 = 0;
        int t, t1 = 0, t2 = 1;
        int r, r1 = m, r2 = n, q;
        while( r2 > 0){
            q = r1 / r2;
            r = r1 - q * r2;
            r1 = r2;
            r2 = r;
            s = s1 - q * s2;
            s1 = s2;
            s2 = s;
            t = t1 - q * t2;
            t1 = t2;
            t2 = t;
        }
        int value = s1 * m + t1 * n;
        if (r1 == value){
            System.out.println("Values of s & t are : " +s1+" "+t1);
        }else{
            System.out.println("Unable to find the values of S and T");
        }
    }
}