//programmer: Nickj.clark14@gmail.com
//date: 2021 11 10

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
    string userFile;
    string line;
    int startingLine;
    

    int number_of_lines = 0;
    ifstream myfile("txt.txt");

    while (getline(myfile, line)) 
        ++number_of_lines;
    cout << "Number of lines in text file: " << number_of_lines << endl; 

    startingLine = number_of_lines - 9;


   	//system pause and return to close main
    system("Pause");
	return 0;
}