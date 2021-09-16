package assignment3;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Program3Sum {

	public static void main(String[] args) {
		
		//declare variables

		int NCNumbers = 0;
		int NCNewNumber = 0;
		int NCTotal = 0;
		int NCCounter= 0;

		
		//create scanner
		Scanner scanner = new Scanner(System.in);
		
		//set up try/catch
		try {
			
		//get user input
		System.out.println("how many numbers would you like to input?: ");
		NCNumbers = scanner.nextInt();
		

		
				
		
		
		//calculate total
		while (NCCounter < NCNumbers) {
		
			System.out.println("Please enter a number: ");
			NCNewNumber = scanner.nextInt();
			
			//add numbers
			NCTotal = NCTotal + NCNewNumber;
			NCCounter ++;

			
		}
			
			
			
		//display total
		System.out.printf("The total is :" + NCTotal);
		
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
