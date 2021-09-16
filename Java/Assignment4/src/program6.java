// programmer: nickj.clark14@gmail.com
// date: 2021 03 08
// modi date:
// purpose: The purpose of this program is to compute the sum of the digits in an integer

// import statements
import java.util.Scanner;

public class program6 {

	// main function
	public static void main(String[] args)     {
		
		// open scanner
	      Scanner scanner = new Scanner(System.in);
	      
	      // get input from user
	      System.out.print("Input an integer: ");
	      int NCdigits = scanner.nextInt();
	      
	      // output results to user
		  System.out.println("The sum is " + sumDigits(NCdigits));
		  
		  // close scanner
		  scanner.close();
	    }

	// find and return sum of digits
	 public static int sumDigits(long n) {
			int NCsum = 0;
			
			// while loop
			while(n > 0) {
				NCsum += n % 10;
				n /= 10;
			}
			
			// return sum to main
			return NCsum;
		}
		
	 }