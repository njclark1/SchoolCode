// programmer: nickj.clark14@gmail.com
// date: 2021 03 08
// modi date:
// purpose: The purpose of this program is to compute the average of three numbers

// import statements
import java.util.Scanner;

public class program2 {

	// main function
	public static void main(String[] args)     {
		
		// open scanner
        Scanner scanner = new Scanner(System.in);
        
        // ask user for input
        System.out.print("Input the first number: ");
        double NCnumber1 = scanner.nextDouble();
        System.out.print("Input the second number: ");
        double NCnumber2 = scanner.nextDouble();
        System.out.print("Input the third number: ");
        double NCnumber3 = scanner.nextDouble();
        
        // output result to user
        System.out.print("The average value is " + NCaverage(NCnumber1, NCnumber2, NCnumber3)+"\n" );
        
        // close scanner
        scanner.close();
    }

	// calculating function
  public static double NCaverage(double NCnumber1, double NCnumber2, double NCnumber3)
    {
	  // return average to main function
        return (NCnumber1 + NCnumber2 + NCnumber3) / 3;
    }
}