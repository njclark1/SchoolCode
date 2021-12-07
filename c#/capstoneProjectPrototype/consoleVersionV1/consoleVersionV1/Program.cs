//programmer: nickj.clark14@gmail.com
//date: 12/7/2021
using System;
using System.IO;

namespace Grader;

class Program
{
    //main function
    static void Main(string[] args)
    {
        //introduce program to user
        Console.WriteLine("Hello, this program will grade your exam");

        //call functiton to read student answer file
        readStudentFile();

        //call function to read correct answer file
        readCorrectFile();

    }//end main function

    //function to parse student answer file
    static void readStudentFile()
    {
        //variables
        string studentPath = "correctAnswers.txt";

        //read file
        if (!File.Exists(studentPath))
        {
            Console.WriteLine("yay!");
            File.CreateText("results.txt");
        }
    }//end readstudentfile

    //function to parse correct answer file
    static void readCorrectFile()
    {
        //variables
        string correctPath = "correctAnswers.txt";

        //read file
        if (!File.Exists(correctPath))
        {
            Console.WriteLine("yay!");
            File.CreateText("results.txt");
        }
    }//end readcorrectfile
}//end program

