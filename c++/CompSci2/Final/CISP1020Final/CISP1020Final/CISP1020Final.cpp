
//programmer: Nickj.clark14@gmail.com
//date: 2021 12 02

/*
For the final assignment, write a program that lets the user convert pounds to kilogramsand kilograms
to pounds.

Use function prototypes in your coding, and include a menu that will allow the user to
choose which conversion to perform, input 2 variables, and then output the result of the conversion.

Put the code in the Dropbox by Dec. 7, 2021.

function for menu to call conversion functions
function to convert lbs to kgs
function to convert kgs to lbs
use prototypes for each function
output the results to user
*/

//include statements
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cstring>

//namespaces
using namespace std;

//prototypes
double convertLbsToKgs(double);
double convertKgsToLbs(double);
void userMenuFunction(int);

int main()
{

    //declare variables
    int conversionPicker = 0;
    double valueToConvert = 0.00;

    //output results to user
    cout << "Hello, this program converts lbs to kgs or vice versa" << endl;
    userMenuFunction(conversionPicker);

    //system pause and return to close main
    system("Pause");
    return 0;
}

void userMenuFunction(int conversionPicker) {
    cout << "Press 1 to covert from Lbs to Kgs, or 2 to convert from Kgs to Lbs" << endl;
    cin >> conversionPicker;
    if (conversionPicker == 1) {
        double lbsToConvert = 0.00;
        cout << "How many lbs would you like to convert to kgs?: " << endl;
        cin >> lbsToConvert;
        double numKgs = convertLbsToKgs(lbsToConvert);
        cout << "The number of Kgs is " << numKgs << endl;
    }
    else if (conversionPicker == 2) {
        double kgsToConvert = 0.00;
        cout << "How many kgs would you like to convert to lbs?: " << endl;
        cin >> kgsToConvert;
        double numLbs = convertKgsToLbs(kgsToConvert);
        cout << "The number of Lbs is " << numLbs << endl;
    }
}

double convertLbsToKgs(double lbsToConvert) {
    double numKgs = 0.00;
    double lbsInKg = 2.205;
    cout << "conversion to kgs called" << endl;
    numKgs = lbsToConvert / lbsInKg;
    return numKgs;
}

double convertKgsToLbs(double kgsToConvert) {
    double numLbs = 0.00;
    double lbsInKg = 2.205;
    cout << "conversion to lbs called" << endl;
    numLbs = kgsToConvert * lbsInKg;
    return numLbs;
}
