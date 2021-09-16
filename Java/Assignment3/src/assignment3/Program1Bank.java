package assignment3;

import java.util.Scanner;

public class Program1Bank {

	public static void main(String[] args) {
		
		//declare variables
			double NCFees = 0;
			int NCChecks = 0;
		
		//create scanner
		Scanner scanner = new Scanner(System.in);
		
		//set up try/catch
		try {
			
		//get user input
		System.out.println("How many checks did you write this month?: ");
		NCChecks = scanner.nextInt();
			
		//calculate fees
		if (NCChecks <= 25)
			NCFees = NCChecks * 0.15 + 12;
		else if (NCChecks >= 26 && NCChecks <= 50)
			NCFees = NCChecks * 0.10 + 12;
		else if (NCChecks > 51)
			NCFees = NCChecks * 0.04 + 12;
			
		//display output to user
		System.out.printf("Your monthly banking fees are $%.2f.%n", NCFees);
		
		}
			
		//catch exceptions
		catch (Exception e) {
			System.out.println("An exception has occured: " + e.getMessage());
		}
		
		finally {
			//close scanner
			if(scanner !=null)
				scanner.close();
		}
			
			
		}
		

}
