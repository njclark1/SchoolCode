//programmer: Nickj.clark14@gmail.com
//date: 2021 10 27

//include statements
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cstring>

//namespaces
using namespace std;

//prototypes
int calcNumWords(const char *);

//main
int main() {

    //declare variables
    char sentence[] = "";
    int sentNumWords = 0;

    //ask user for input
    cout << "What is your string?" << endl;
    cin.getline(sentence, 10000);

    //pass input to calculation function
    sentNumWords = calcNumWords(sentence);

    //output results to user
    cout << "The number of words in your string is " << sentNumWords << endl;
   	//system pause and return to close main
    system("Pause");
	return 0;
}

//function to calculate number of words in a string
int calcNumWords(const char *sentence) {
    int count = strlen(sentence);
    int numWords = 1;
    for (int i = 0; i < count; i++)
    {
        if (sentence[i] == ' ')
        numWords ++;
    }
    return numWords;
}
