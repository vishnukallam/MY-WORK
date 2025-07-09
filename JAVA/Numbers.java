import java.util.*;
public class exception {
    public static void main(String[] args) {
     int i,j,k;
     Scanner s = new Scanner(System.in);
        try {
            throw();

         if (i < 18 ){
             System.out.println("you are not have to vote");
         }
         else{
             System.out.println("U have right to vote");
         }
     }
        catch (Exception e){
            System.out.println("Exception" + e);
        }
        finally {
            System.out.println("The code is executed");
        }
    }
}
