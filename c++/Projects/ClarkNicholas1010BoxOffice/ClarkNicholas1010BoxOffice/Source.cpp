// programmer: nickj.clark14@gmail.com
// date: 2021 02 09
// modi date: 2021 02 11
// purpose: This is a program that calculates the revenue for a box office


#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main() {

    //need 9 variables

    //declare constants
    const double ADULT_TICKET_PRICE = 10.00, CHILD_TICKET_PRICE = 6.00,
        THEATER_PERCENT_REVENUE = .20, DISTRIBUTOR_PERCENT_REVENUE = .80;

    //declare variables
    int adultTicketsSold, childTicketsSold;
    double grossBoxOfficeProfit, netBoxOfficeProfit, distributorPayment;

    string movieName = "";

    //output program purpose

    cout << "\nThis is a program that calculates the revenue for a box office.\n";

    //ask user for movie name
    cout << "\nWhat is the name of the movie?: ";
    getline(cin, movieName);

    //ask user for adult tickets sold
    cout << "\nHow many adult tickets were sold?: ";
    cin >> adultTicketsSold;

    //ask user for child tickets sold
    cout << "\nHow many child tickets were sold?: ";
    cin >> childTicketsSold;

    //calculate gross box office revenue
    grossBoxOfficeProfit = (adultTicketsSold * ADULT_TICKET_PRICE) + (childTicketsSold * CHILD_TICKET_PRICE);

    //calculate distributor cost
    distributorPayment = grossBoxOfficeProfit * DISTRIBUTOR_PERCENT_REVENUE;

    //calculate net box office profit
    netBoxOfficeProfit = grossBoxOfficeProfit - distributorPayment;

    //output data to user
    cout << "\nMovie Name: \t\t" << "\"" << movieName << "\"" << endl;
    cout << "Adult Tickets Sold: \t\t" << adultTicketsSold << endl;
    cout << "Child Tickets Sold: \t\t" << childTicketsSold << endl;
    cout << fixed << setprecision(2) << "Gross Box Office Profit: \t" << "$" << grossBoxOfficeProfit << endl;
    cout << "Net Box Office Profit: \t\t" << "$" << netBoxOfficeProfit << endl;
    cout << "Amount Paid to Distributors: \t" << "$" << distributorPayment << endl;

    system("Pause");
    return 0;
}