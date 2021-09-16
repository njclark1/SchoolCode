// programmer: nickj.clark14@gmail.com
// date: 2021 03 08
// modi date:
// purpose: The purpose of this program is to to count all words in a string

// import statements
import java.util.Scanner;

public class program5 {

	// main function
	public static void main(String[] args)     {
		
		// open scanner
        Scanner scanner = new Scanner(System.in);
        
        // get input from user
        System.out.print("Input the string: ");
        String str = scanner.nextLine();
        
        // output results to user
        System.out.print("Number of words in the string: " + count_Words(str)+"\n");
        
        // close scanner
        scanner.close();
    }

	
	// calculating function
 public static int count_Words(String str)
    {
       int count = 0;
       
       // if statement
        if (!(" ".equals(str.substring(0, 1))) || !(" ".equals(str.substring(str.length() - 1))))
        {
        	
        	// for loop
            for (int NCInteger = 0; NCInteger < str.length(); NCInteger++)
            {
            	
            	// if statement
                if (str.charAt(NCInteger) == ' ')
                {
                    count++;
                }
            }
            count = count + 1; 
        }
        
        // return count to main
        return count; 
    }
 }