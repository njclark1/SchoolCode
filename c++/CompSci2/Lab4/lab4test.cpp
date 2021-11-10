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
string getInput();
int getNumLines(string);

//main
int main() {
    //declare variables
    string line;
    int startingLine;
    int number_of_lines = 0;
    bool showMessage = false;
    string message = "The entire file has been output";

    //get user input
    string userFile = getInput();

    //get number of lines
    int numberLines = getNumLines(userFile);


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

//get user input
string getInput() {
    string userInput;
    cout << "what is your file name?" << endl;
    cin >> userInput;
    return userInput;
}

//get number of lines
int getNumLines(string userFile) {
    //open file for count
    string line;
    int numLines;
    fstream textFileCount(userFile);
    //get number of lines in file
    while (getline(textFileCount, line)) {
        numLines++;
        
    }
    return numLines;
}
