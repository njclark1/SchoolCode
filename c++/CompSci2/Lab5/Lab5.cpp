//programmer: Nickj.clark14@gmail.com
//date: 2021 11 16

//include statements
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cstring>
#include <fstream>


//namespaces
using namespace std;

//prototypes


//main
int main() {

    //declare variables
    string myString = "";
    //logic
    cout << "What is your string?: " << endl;
    getline(cin, myString);
    //output results to user


    cout << myString;
   	//system pause and return to close main
    system("Pause");
	return 0;
}

void reverseStr(string myString) {
    if (myString.size() == 0)
    {
        return;
    }
    cout << myString[0];
}