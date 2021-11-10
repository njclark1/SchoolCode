//programmer: Nickj.clark14@gmail.com
//date: 2021 10 28

//include statements
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cstring>

//namespaces
using namespace std;

//prototypes
int calcNumDigits(const char *);
int calcNumUpper(const char *);
int calcNumLower(const char *);

//main
int main()
{

    //declare variables
    char sentence[] = "";
    int passNumDigits = 0;
    int passNumChar = 0;
    int passNumUpper = 0;
    int passNumLower = 0;

    //ask user for input
    cout << "Your password must contain 6 characters, one upper case letter, one lower case letter, and one numeric digit." << endl;
    cout << "What is your password?" << endl;
    cin.getline(sentence, 10000);

    //pass input to calculation function
    //numeric digits
    passNumDigits = calcNumDigits(sentence);
    //upper case
    passNumUpper = calcNumUpper(sentence);
    //lower case
    passNumLower = calcNumLower(sentence);
    //length requirement
    passNumChar = strlen(sentence);

    while (passNumDigits < 1 || passNumChar < 6 || passNumUpper < 1 || passNumLower < 1)
    {
        string errorOutput = "Unmet credentials:";

        if (passNumChar < 6) {
            errorOutput += " at least 6 characters.";
        }
        if (passNumDigits < 1) {
            errorOutput += " at least one digit.";
        }
        if (passNumUpper < 1) {
            errorOutput += " at least one Upper case letter.";
        }
        if (passNumLower < 1) {
            errorOutput += " at least one Lower case letter.";
        }

        errorOutput += "\nPlease try a different password that meet all criteria.";

        //ask user for input
        cout << errorOutput << endl;
        cin.getline(sentence, 10000);
        //pass input to calculation function
        //numeric digits
        passNumDigits = calcNumDigits(sentence);
        //upper case
        passNumUpper = calcNumUpper(sentence);
        //lower case
        passNumLower = calcNumLower(sentence);
        //length requirement
        passNumChar = strlen(sentence);

    }

    //output results to user
    cout << "\nGreat! Your password has been accepted!" << endl;
    //system pause and return to close main
    system("Pause");
    return 0;
}

//function to calculate number of upper case lettter
int calcNumDigits(const char *sentence)
{
    int count = strlen(sentence);
    int numDigits = 0;
    for (int i = 0; i < count; i++)
    {
        if (isdigit(sentence[i]))
            numDigits++;
    }
    return numDigits;
}

//function to calculate number of upper case lettter
int calcNumUpper(const char *sentence)
{
    int count = strlen(sentence);
    int numUpper = 0;
    for (int i = 0; i < count; i++)
    {
        if (isupper(sentence[i]))
            numUpper++;
    }
    return numUpper;
}
//function to calculate number of lower case letters
int calcNumLower(const char *sentence)
{
    int count = strlen(sentence);
    int numLower = 0;
    for (int i = 0; i < count; i++)
    {
        if (islower(sentence[i]))
            numLower++;
    }
    return numLower;
}
