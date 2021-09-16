// Chapter 3 - Programming Challenge 10,  Box Office
// This program calculates a theaters's Gross and net profit.
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;



int main()



{
    //variables
       // three catagories : double/const, double, int
    double grossBox, netBox, distPaid;
    const double  REVENUE_PERCENT = .8, DIST_PERCENT = .2, CHILD_TICKET = 6, ADULT_TICKET = 10;
    int childTickets, adultTickets;
    string movieName;
    // total number of all three data types combined: xx
    // const double: 4
    // int: kids, adults



 //string
    // string nameOfMovie



 //get Input from user: movie name
 //cout ,getline(cin moviename );
    cout << "what is the movie name?";
    cin >> movieName;
    //adults tickets
    cout << "How many adult tickets was sold?";
    cin >> adultTickets;
    //child tickets
    cout << "How many child tickets was sold?";
    cin >> childTickets;
    //Calculate Gross and net profits and distrbutor paymnet
    grossBox = (adultTickets * ADULT_TICKET) + (childTickets * CHILD_TICKET);
    distPaid = grossBox * .20;
    netBox = grossBox - distPaid;
    // gross,net,dist



    //display results "cls"
    cout << "Gross Pay $" << (adultTickets * ADULT_TICKET) + (childTickets * CHILD_TICKET) << endl;
    cout << "Dist Pay $" << grossBox * .20 << endl;
    cout << "Net Pay $" << grossBox - distPaid << endl;



    system("pause");
    return 0;
}