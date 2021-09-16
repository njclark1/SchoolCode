package Chapter3and4;

// programmer: nickj.clark14@gmail.com
// date: 2021 02 06
// modi date:
// purpose: This program calculates the sum and average of two integer inputs


import java.util.Scanner;

public class SumAvg {

	   public static void main(String[] args) {

	       // output program purpose
	       System.out.println("This program calculates the sum and average of two integer inputs");

	       // get integer 1
	       System.out.println("What is the first integer? ");
	       Scanner NCScannerOne = new Scanner(System.in);
	       int NCIntegerOne = NCScannerOne.nextInt();

	       // get integer 2
	       System.out.println("What is the second integer? ");
	       Scanner NCScannerTwo = new Scanner(System.in);
	       int NCIntegerTwo = NCScannerTwo.nextInt();

	       int NCIntegerSum = NCIntegerOne + NCIntegerTwo;
	       double NCIntegerAverage = ((float)NCIntegerOne + (float)NCIntegerTwo) / 2;

	       // Output the calculations
	       System.out.println("The sum is " + NCIntegerSum + ", and the average is " + NCIntegerAverage + ".");
	       NCScannerOne.close();
	       NCScannerTwo.close();
	   }
	}

