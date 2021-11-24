//programmer: Nickj.clark14@gmail.com
//date: 2021 11 11

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
    bool showMessage = false;
    string message = "The entire file has been output";

    //get user input
    cout << "This program will ready a text file and output the last ten lines." << endl;
    cout << "what is your file name, including the file type extension?" << endl;
    cin >> userFile;

    fstream textFileCount(userFile);
    //get number of lines in file
    while (getline(textFileCount, line)) {
        ++number_of_lines;
    }

    //get line to start printing
    startingLine = number_of_lines - 10;
    if (startingLine <= 0) {
        startingLine = 0;
        showMessage = true;
    }

    //open file again to print
    fstream textFilePrint(userFile);

    //move file to line we are starting our print on
    for(int i=0 ; i<startingLine ; i++) {
        getline(textFilePrint, line);
    }

    //print rest of file
    while(std::getline(textFilePrint, line)) {
        std::cout<<line<<'\n';
    }

    //print message to user if full file output
    if (showMessage == true) {
        cout << message << endl;
    }

   	//system pause and return to close main
    system("Pause");
	return 0;
}