
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
float convertLbsToKgs(float);
float convertKgsToLbs(float);
void userMenuFunction(int);

int main()
{

    //declare variables
    int conversionPicker = 0;
    float valueToConvert = 0.00;

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
        float lbsToConvert = 0.00;
        cout << "How many lbs would you like to convert to kgs?: " << endl;
        cin >> lbsToConvert;
        float numKgs = convertLbsToKgs(lbsToConvert);
        cout << "The number of Kgs is " << numKgs << endl;
    }
    else if (conversionPicker == 2) {
        float kgsToConvert = 0.00;
        cout << "How many kgs would you like to convert to lbs?: " << endl;
        cin >> kgsToConvert;
        float numLbs = convertKgsToLbs(kgsToConvert);
        cout << "The number of Lbs is " << numLbs << endl;
    }
}

float convertLbsToKgs(float lbsToConvert) {
    float numKgs = 0.00;
    float lbsInKg = 2.205;
    cout << "conversion to kgs called" << endl;
    numKgs = lbsToConvert / lbsInKg;
    return numKgs;
}

float convertKgsToLbs(float kgsToConvert) {
    float numLbs = 0.00;
    float lbsInKg = 2.205;
    cout << "conversion to lbs called" << endl;
    numLbs = kgsToConvert * lbsInKg;
    return numLbs;
}
