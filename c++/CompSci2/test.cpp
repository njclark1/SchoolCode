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

int calcNumWords(string);

int main() {

    char sentence[] = "";
    cout << "W" << endl;
    cin.getline(sentence, 10000000000000);


    //cout << "What is your string?";
    //cin >> sentence;
   // int sentenceLength = sentence.length();
    //char *pStr = new char[sentenceLength];

    //cout << *pStr << endl;
  //  cout << sentenceLength << endl;
    cout << sentence << endl;
    cout << strlen(sentence) << endl;;

   	//system pause and return to close main
    system("Pause");
	return 0;
}
