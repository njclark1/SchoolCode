package testing;

import javax.swing.JOptionPane;

public class testing {

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