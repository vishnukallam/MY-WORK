import java.util.Scanner;
public class Armstrong {
    public static void main(String[] args) {
        int n,temp, sum=0;
        Scanner s = new Scanner(System.in);
       System.out.println("enter the value of n : ");
       n = s.nextInt();
       String str = String.valueOf(n);
       int len = str.length();
       temp = n;
       while (temp!=0){
           int rem = temp%10;
           sum += (double)Math.pow(rem,len);
           temp /= 10;
       }
        System.out.println(sum);
       if (sum == n){
           System.out.println("The given number "+ n + " is an armstrong number.");
       }
       else{
           System.out.println("The given number " + n + " is not an armstrong number.");
       }

    }
}
