//programmer: Nickj.clark14@gmail.com
//date: 2021 02 18
//modi date:
//purpose: This program calculates the discount and total cost of an order

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main()
{
	const double RETAIL_COST = 199.00;  // Normal retail price per unit before discount
	int unitsPurchased;				   // Number of units purchased
	double discountPct,				   // % discount based on sales volume
		totalCost;					   // Total cost (for all units purchased) after discount

	// get number purchased from user
	cout << "To get an estimate, please enter between 1 and 100\n" << endl;
	cout << "How many units are being purchased? ";
	cin >> unitsPurchased;

	// start if statement
	if (unitsPurchased < 1 || unitsPurchased > 100) // Incorrect value
	{
		cout << "The number MUST be from 1-100" << endl;
		cout << "Please enter a correct value" << endl;
		cin >> unitsPurchased;


		if (unitsPurchased < 1 || unitsPurchased > 100)
		{
			cout << "The number entered is incorrect again. Please email: nickj.clark14@gmail.com" << endl;
			system("pause");
			exit(1); // breaks out of code, and quit
		}
	}
	else
	{
		// welcome user to program
		cout << "\nWelcome to the Software Purchase Program\n" << endl;

	}

	// if statements for quantity discount
	if (unitsPurchased < 10 )
	{
		discountPct = 0.00;		// quan < 10
	}

	else if (unitsPurchased <= 19 )
	{
		discountPct = 0.20;		// quan 10-19
	}

	else if (unitsPurchased <= 49 )
	{
		discountPct = 0.30;		// quan 20-49
	}

	else if (unitsPurchased <= 99 )
	{
		discountPct = 0.40;		// quan 20-49
	}

	else
	{
		discountPct = 0.50;		// quan 100
	}

	// calculate the total cost
	totalCost = (RETAIL_COST * unitsPurchased) - ((RETAIL_COST * unitsPurchased) * discountPct);

	// display outputs to user
	cout << setw(36) << left << "Unit Quantity: " << right << unitsPurchased << endl;
	cout << setw(35) << left << "Discount Percentage: " << right << discountPct * 100 << "%" << endl;
	cout << setw(30) << left << "Total Cost: " << right << fixed << setprecision(2) << "$" << totalCost << endl;
	system("Pause");
	return 0;
}