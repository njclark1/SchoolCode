// programmer: nickj.clark14@gmail.com
// date: 2021 03 08
// modi date:
// purpose: The purpose of this program is to count all vowels in a string

// import statements
import java.util.Scanner;

public class program4 {

	// main function
	public static void main(String[] args)     {
		
		// open scanner
        Scanner scanner = new Scanner(System.in);
        
        // get input from user
        System.out.print("Input the string: ");
        String str = scanner.nextLine();
        
        // output results to user
        System.out.print("Number of  Vowels in the string: " + count_Vowels(str)+"\n");
        
        // close scanner
        scanner.close();
    }
	
	// calculating function
 public static int count_Vowels(String str)
    {
        int count = 0;
        
        // for loop
        for (int NCinteger = 0; NCinteger < str.length(); NCinteger++)
        {
        	
        	// if statement
            if (str.charAt(NCinteger) == 'a' || str.charAt(NCinteger) == 'e' || str.charAt(NCinteger) == 'i'
                    || str.charAt(NCinteger) == 'o' || str.charAt(NCinteger) == 'u')
            {
                count++;
            }
        }
        
        // return count to main
        return count;
    }
}