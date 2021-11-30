//programmer: nickj.clark14@gmail.com
//date: 11 29 2021

//problem 1
//need iostream for cout
#include <iostream>

//problem 2
//need std for cout
using namespace std;

class  MyClass
{
public:
//problem 3
//need function return type, in this case "void"
virtual void myFun() 
//probem 4
//function is not a variable to be set to an integer. Unless I'm missing something, I don't see a reason for this.
{
    //problem 5
    //incorrect quotation marks for string.
    cout << "Hello";

    }
};

/*
class  MyClass
{
public:
virtual void myFun( ) = 0;
{
    cout << "Hello";
    }
};
*/
