package Chapter3and4;

//programmer: nickj.clark14@gmail.com
//date: 2021 02 05
//modi date:
//purpose:

import java.util.Scanner;
import java.lang.Math;

public class Perimeter {

	   public static void main(String[] args) {

	       //output welcome message
	       System.out.println("This program calculates the perimeter and area of a given radius.\n");

	       //get radius from user
	       System.out.println("What is the radius? ");
	       Scanner NCScanner = new Scanner(System.in);
	       double NCRadius = NCScanner.nextDouble();

	       //calculate perimeter
	       double NCPerimeter = (2 * Math.PI) * NCRadius;

	       //calculate area
	       Double NCArea = Math.PI * Math.pow(NCRadius, 2);

	       //output perimeter
	       System.out.println("\nThe perimeter is " + NCPerimeter + "\n");

	       //output area
	       System.out.println("The area is " + NCArea);
	       NCScanner.close();

	   }
	}
