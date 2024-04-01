import java.util.Scanner;
public class ifclass {
    public static void main(String[] args) {
        int i = 0,n,temp, sum=0;
        Scanner s = new Scanner(System.in);
       System.out.println("enter the value of n : ");
       n = s.nextInt();
       String str = String.valueOf(n);
       int len = str.length();
       temp = n;
       while (temp!=0){
           int rem = temp%10;
           sum += Math.pow(rem,len);
           temp /= 10;
       }
       if (sum == n){
           System.out.println("The given number "+ n + " is an armstrong number.");
       }
       else{
           System.out.println("The given number " + n + " is not an armstrong number.");
       }

    }
}
