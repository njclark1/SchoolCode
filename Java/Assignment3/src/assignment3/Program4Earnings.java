package assignment3;

import java.util.Scanner;
import java.util.InputMismatchException;

public class Program4Earnings {

	public static void main(String[] args) {
		
		//declare variables
		int NCPennies = 0;
		int NCPay = 0;
		int NCDays= 0;
		int NCCounter= 0;

		
		//create scanner
		Scanner scanner = new Scanner(System.in);
		
		//set up try/catch
		try {
			
		//get user input
		System.out.println("What is the number of days?(1-31): ");
		NCDays= scanner.nextInt();
		
		NCCounter = 1;
		NCPennies = 1;
		NCPay = 0;
				
		
		
		//calculate fees
		while (NCCounter <= NCDays) {
		
			//Display pennies earned
			System.out.println("Day " + NCCounter + "\t \t \t \t" + NCPennies + "\tPennies");
			
			//accumulate pennies
			NCPay = NCPay + NCPennies;
			NCCounter ++;
			
			//double the pennies
			NCPennies = NCPennies *2;
			
		}
			
			
			
		//display pay
		System.out.printf("The total pay is: $" + NCPay/100.0);
		
		}
			
		//catch mismatch exceptions
		catch (InputMismatchException e) {
			System.out.println("please enter an integer.");
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


