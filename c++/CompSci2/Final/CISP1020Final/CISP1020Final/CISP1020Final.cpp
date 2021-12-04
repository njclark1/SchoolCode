
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

//namespaces
using namespace std;

//prototypes
double convertLbsToKgs(double);
double convertKgsToLbs(double);
void userMenuFunction(int);

//main function
int main()
{
    //declare variables
    int conversionPicker = 0;
    double valueToConvert = 0.00;

    //output introduction to user
    cout << "Hello, this program converts lbs to kgs or vice versa" << endl;

    //call menu function
    userMenuFunction(conversionPicker);

    //system pause and return to close main
    system("Pause");
    return 0;
}

//menu function for user to choose conversion
void userMenuFunction(int conversionPicker) {
    cout << "Press 1 to covert from Lbs to Kgs, or 2 to convert from Kgs to Lbs" << endl;
    cin >> conversionPicker;
    //logic to call conversion from lbs to kgs
    if (conversionPicker == 1) {
        double lbsToConvert = 0.00;
        cout << "How many lbs would you like to convert to kgs?: " << endl;
        cin >> lbsToConvert;
        double numKgs = convertLbsToKgs(lbsToConvert);

        //output final result to user
        cout << "The number of Kgs is " << numKgs << endl;
    }
    //logic to call conversion from kgs to lbs
    else if (conversionPicker == 2) {
        double kgsToConvert = 0.00;
        cout << "How many kgs would you like to convert to lbs?: " << endl;
        cin >> kgsToConvert;
        double numLbs = convertKgsToLbs(kgsToConvert);

        //output final result to user
        cout << "The number of Lbs is " << numLbs << endl;
    }
}

//function to convert from lbs to kgs
double convertLbsToKgs(double lbsToConvert) {
    //variables
    double numKgs = 0.00;
    double kgsInLb = 0.45359237;
    //conversion math
    numKgs = lbsToConvert * kgsInLb;
    //return answer
    return numKgs;
}

//function to convert from kgs to lbs
double convertKgsToLbs(double kgsToConvert) {
    //variables
    double numLbs = 0.00;
    double kgsInLb = 0.45359237;
    //conversion
    numLbs = kgsToConvert / kgsInLb;
    //return answer
    return numLbs;
}
