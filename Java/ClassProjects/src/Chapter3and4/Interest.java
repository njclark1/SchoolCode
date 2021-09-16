package Chapter3and4;

//programmer: nickj.clark14@gmail.com
//date: 2021 02 05
//modi date:
//purpose: This program calculates the compound interest of a loan

import java.util.Scanner;

public class Interest {

	   public static void main(String[] args) {

	       // output program purpose
	       System.out.println("This program calculates the compound interest of a loan");

	       // Get principal amount
	       System.out.println("What is the Principal Amount? $");
	       Scanner NCScanner = new Scanner(System.in);
	       double NCPrincipalAmount = NCScanner.nextLong();

	       // get interest rate
	       System.out.println("What is the Interest Rate? ");
	       double NCInterestRate = NCScanner.nextDouble();

	       // get time period
	       System.out.println("What is the Time Period? ");
	       double NCTimePeriod = NCScanner.nextDouble();

	       // calculate the compound interest
	       double NCCompoundInterest = NCPrincipalAmount * Math.pow((1 + NCInterestRate / 100), NCTimePeriod);

	       // Output the compound interest
	       System.out.println("The Compound Interest is: $" + NCCompoundInterest);
	       NCScanner.close();
	   }
	}
