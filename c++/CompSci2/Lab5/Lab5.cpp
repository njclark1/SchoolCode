//programmer: Nickj.clark14@gmail.com
//date: 2021 11 24

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
void reverseStr(string);

//main
int main() {

    //declare variables
    string myString = "";

    //logic
    //get input from user
    cout << "What is your string?: " << endl;
    getline(cin, myString);

    //call function to print reverse string
    reverseStr(myString);

    //output results to user
    cout << myString;

   	//system pause and return to close main
    system("Pause");
	return 0;
}//end main

// function definition
void reverseStr(string myString) {

    //size of string
  size_t numChar = myString.size();

    //print each char
  if(numChar == 1) {
    cout << myString << endl;
  }
  else {
    cout << myString[numChar - 1];

    //recursion of function
    reverseStr(myString.substr(0, numChar - 1));
  }
}//end reverseStr