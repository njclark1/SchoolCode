// programmer: nickj.clark14@gmail.com
// date: 2021 01 26
// modi date:
// purpose: add a set of numbers, multiple a set of numbers

#include <iostream>;
using namespace std;

int main()
{
	double hours, rate, pay;

	// Get number of hours worked.
	cout << "How many hours did you work? ";
	cin >> hours;

	// Get the hourly pay rate.
	cout << "How much do you get paid per hour? ";
	cin >> rate;

	// Calculate the pay.
	pay = hours * rate;

	// Display the pay.
	cout << "You have earned $" << pay << endl;
	return 0;
}