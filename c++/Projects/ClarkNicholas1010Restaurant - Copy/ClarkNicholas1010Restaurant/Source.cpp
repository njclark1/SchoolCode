// programmer: nickj.clark14@gmail.com
// date: 2021 02 02
// modi date:
// purpose: This program calculates the tax, tip, and total bill at a restaurant

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double mealCharge, taxRate, taxAmount, taxAdded, tipRate, tipAmount, totalBill;
    mealCharge = 44.50;
    taxRate = .0675;
    tipRate = .15;

    //calculate meal tax amount
    taxAmount = mealCharge * taxRate;
    //calculate meal cost after tax
    taxAdded = mealCharge + taxAmount;
    //calculate tip amount
    tipAmount = taxAdded * tipRate;
    //calculate total bill
    totalBill = taxAdded + tipAmount;

    //display results

    //display : $meal cost, %tax rate, %tip rate
    //display : results from calcs, total amount, tip amount, tax amount
    //display : welcome 
    cout << "Welcome! This program will calculate a restaurant bill.\n";
    //meal cost
    cout << "The meal cost is $" << setprecision(2) << fixed << mealCharge << "." << endl;
    //tax rate
    cout << "The tax rate is " << setprecision(2) << fixed << taxRate * 100 << "%." << endl;
    //tip rate
    cout << "The tip rate is " << setprecision(0) << fixed << tipRate * 100 << "%." << endl;
    //tax amount
    cout << "The tax amount is $" << setprecision(2) << fixed << taxAmount << "." << endl;
    //tip amount
    cout << "The tip amount is $" << setprecision(2) << fixed << tipAmount << "." << endl;
    //total bill
    cout << "The total bill is $" << setprecision(2) << fixed << totalBill << "." << endl;
    system("Pause");
    return 0;
}

/* CORRECT RESULTS
meal costs  - $44.5
tax amt     - $3.00375
tip amt     - $7.12556
total amt   - $54.6293
*/

