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

int calcNumWords(const char *);

int main() {

    //declare variables
    char sentence[] = "";
    int sentNumWords = 0;

    //ask user for input
    cout << "What is your string?" << endl;
    cin.getline(sentence, 10000);

    sentNumWords = calcNumWords(sentence);

    //output results to user
    cout << "The number of words in your string is " << sentNumWords + 1 << endl;
   	//system pause and return to close main
    system("Pause");
	return 0;
}

int calcNumWords(const char *sentence) {
    int count = strlen(sentence);
    int numWords = 0;
    for (int i = 0; i < count; i++)
    {
        if (sentence[i] == ' ')
        numWords ++;
    }
    return numWords;
}