// programmer: nickj.clark14@gmail.com
// date: 2021 01 28
// modi date:
// purpose: This program calculates the total amount spent to
// to make a flower garden.


#include <iostream>;
#include <iomanip>;
using namespace std;

int main()
{
	double soilCost, seedCost, fenceCost, totalSpent;

	// Get the total cost of soil.
	cout << "How much was spent for soil? $";
	cin >> soilCost;

	// Get the total cost of seeds.
	cout << "How much was spent for seeds? $";
	cin >> seedCost;

	// Get the total cost of fencing.
	cout << "How much was spent for the fence? $";
	cin >> fenceCost;

	//  Calculate the sum spent.
	totalSpent = soilCost + seedCost + fenceCost;

	// Display the results.
	cout << "The total amount spent to make the flower garden was $" << setprecision(2) << fixed << totalSpent << endl;
	system("pause");
	return 0;
}

/* SAMPLE RUN RESULTS

This program computes the total amount spent to create a flower garden.

How much was spent for soil? $25
How much was spent for seeds? $10.50
How much was spent for the fence? $21
The total amount spent to make the flower garden was $56.5
*/
