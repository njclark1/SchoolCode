package assignment3;

import javax.management.ValueExp;

public class PrintFPractice {

	public static void main(String[] args) {
		
		boolean myBoolean = true;
		char myChar = '@';
		String myString = "Bro";
		int myInt = 69;
		double myDouble = 400020.69;
		
		
		System.out.printf("The boolean is %b", myBoolean);
		System.out.printf("\nThe char is %c", myChar);
		System.out.printf("\nThe string is %s", myString);
		System.out.printf("\nThe int is %d", myInt);
		System.out.printf("\nThe double is %f", myDouble);
		
		//double with precision
		System.out.printf("\nThe double with precision is %.2f", myDouble);
		
		//width sets the minimum number of characters to display
		System.out.printf("\nHello with width %10s", myString);
		
		//flags baby
		
		//left justify
		System.out.printf("\nHello with width and a left justify %-10s", myString);
		//comma to add commas in number
		System.out.printf("\nThe double with commas is %,f", myDouble);
	}

}
