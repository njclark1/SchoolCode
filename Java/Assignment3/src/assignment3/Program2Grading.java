package assignment3;

import java.util.Scanner;
import java.util.InputMismatchException;

public class Program2Grading {
	

	
	public static void main(String[] args) {
		//declare variables
		String NCGrade1 = "";
		String NCGrade2 = "";
		String NCGrade3 = "";
		String NCGrade4 = "";
		int NCAverage = 0;
		String NCGrade = "";
		
		//create scanner
		Scanner scanner = new Scanner(System.in);
		
	
	
		
		//set up try/catch
		try {
			
		//get user input
		System.out.println("What was the first grade?: ");
		NCGrade1 = scanner.next();
		System.out.println("What was the second grade?: ");
		NCGrade2 = scanner.next();
		System.out.println("What was the third grade?: ");
		NCGrade3 = scanner.next();
		System.out.println("What was the fourth grade?: ");
		NCGrade4 = scanner.next();
		
			
		//convert to int
		int NCTest1 = Integer.parseInt(NCGrade1);
		int NCTest2 = Integer.parseInt(NCGrade2);
		int NCTest3 = Integer.parseInt(NCGrade3);
		int NCTest4 = Integer.parseInt(NCGrade4);
		
		//calculate average grade
		NCAverage = (NCTest1 + NCTest2 + NCTest3 + NCTest4) / 4;
		
		
		//calculate letter grade
		if (NCAverage >= 90)
			NCGrade = "A";
		else if (NCAverage >= 80 && NCAverage <= 89)
			NCGrade = "B";
		else if (NCAverage >= 70 && NCAverage <= 79)
			NCGrade = "C";
		else if (NCAverage >= 60 && NCAverage <= 69)
			NCGrade = "D";
		else if (NCAverage <60)
			NCGrade = "F";
		
		//Display output to user
		System.out.println("Your final grade is " + NCGrade + ".");
		
		}

		
		//catch exceptions
		catch (InputMismatchException e) {
			System.out.println("please enter a valid test grade");
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
