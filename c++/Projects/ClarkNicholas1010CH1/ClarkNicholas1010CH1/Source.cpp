// programmer: nickj.clark14@gmail.com
// date: 2021 01 28
// modi date:
// purpose: This program calculates earnings from candy bar sales.

#include <iostream>;
using namespace std;

int main()
{
	double numSold, earningsPerBar, totalEarnings;
	// Get the number of candy bars sold.
	cout << "How many candy bars were sold? ";
	cin >> numSold;

	// Get the amound earned per bar sold.
	cout << "How much is earned for each bar sold? ";
	cin >> earningsPerBar;

	// Calculate the total earnings.
	totalEarnings = numSold * earningsPerBar;

	// Display the total earnings.
	cout << "You have earned $" << totalEarnings << endl;
	return 0;
}

/* SAMPLE RUN RESULTS
How many candy bars were sold? 210
How much is earned for each bar sold? .15
You have earned $31.5
*/


