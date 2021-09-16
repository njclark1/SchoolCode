// programmer: nickj.clark14@gmail.com
// date: 2021 01 26
// modi date:
// purpose: This program calculates the amount a baseball team spent on baseball purchases.

#include <iostream>;
using namespace std;

int main()
{
	double ballsPurchased, unitCost, totalCost;

	// Get the number of baseballs purchased.
	cout << "How many baseballs were purchased? ";
	cin >> ballsPurchased;

	// Get the cost of each ball.
	cout << "How much did each ball cost? ";
	cin >> unitCost;

	// Calculate the total amount spent.
	totalCost = ballsPurchased * unitCost;

	// Display the total amount spent.
	cout << "The total amount spent on baseballs was $" << totalCost << endl;
	return 0;
}

/* SAMPLE RUN RESULTS
How many baseballs were purchased? 12
How much did each ball cost? 8.95
The total amount spent on baseballs was $107.4
*/
