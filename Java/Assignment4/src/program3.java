// programmer: nickj.clark14@gmail.com
// date: 2021 03 08
// modi date:
// purpose: The purpose of this program is to display the middle character of a string

// import statements
import java.util.Scanner;

public class program3 {
	
	// main function
	public static void main(String[] args)     {
		
		// open scanner
        Scanner scanner = new Scanner(System.in);
        
        // get input from user
        System.out.print("Input a string: ");
        String str = scanner.nextLine();
        
        // output result to user
        System.out.print("The middle character in the string: " + middle(str)+"\n");
        
        // close scanner
        scanner.close();
    }
	
	// calculating function
 public static String middle(String str)
    {
	 
	 // declare variables
        int NCposition;
        int NClength;
        
        // if statement
        if (str.length() % 2 == 0)
        {
        	NCposition = str.length() / 2 - 1;
        	NClength = 2;
        }
        else
        {
        	NCposition = str.length() / 2;
        	NClength = 1;
        }
        
        // return output to main
        return str.substring(NCposition, NCposition + NClength);
    }
}