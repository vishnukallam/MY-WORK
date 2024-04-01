import java.io.IOException;
class ReadData2 {
    public static void main(String []args) throws IOException {
        byte b[]=new byte[80];
        System.out.println("Enter text:");
/*
System.in.read(b,0,80);
System.in.read(b);
These two statements are equal. Use either one.
*/
        System.in.read(b,0,80);
        String s=new String(b);
        System.out.println("You entered text:\""+ s +" \" ");
    }
}