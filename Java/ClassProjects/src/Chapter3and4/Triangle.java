package Chapter3and4;

//programmer: nickj.clark14@gmail.com
//date: 2021 02 05
//modi date: 2021 02 05
//purpose: This program calculates the area of a triangle

import java.lang.Math;
import javax.swing.JOptionPane;


public class Triangle {

	   public static void main(String[] args) {

	       //output welcome message
	       JOptionPane.showMessageDialog(null, "This program calculates the area of a triangle");

	       //get base from user

	       String NCBase = JOptionPane.showInputDialog("What is the base? ");
	       double NCBaseDouble = Double.parseDouble(NCBase);


	       //get height from user
	       String NCHeight = JOptionPane.showInputDialog("What is the height? ");
	       double NCHeightDouble = Double.parseDouble(NCHeight);

	       //calculate area
	       double NCArea = (.5 * NCBaseDouble) * NCHeightDouble;



	       System.out.println(NCArea);

	       JOptionPane.showMessageDialog(null, "The area of the triangle is " + NCArea);
	   }
	}
