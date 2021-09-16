// programmer: nickj.clark14@gmail.com
// date: 2021 01 26
// modi date:
// purpose: add a set of numbers, multiple a set of numbers

#include <iostream>;
using namespace std;

int main()
{
	// variables
	int num1, num2, num3, num4, num12, num34;
	num1 = 10;
	num2 = 20;
	num3 = 30;
	num4 = 40;

	//calculation area
	num12 = num1 + num2;
	num34 = num3 * num4;

	// output area
	cout << "Sum of Number 1 and Number 2 : " << num12 << endl;
	cout << "Product of Number 3 and Number 4 : " << num34 << endl;

	system("pause");
	return 0;

}