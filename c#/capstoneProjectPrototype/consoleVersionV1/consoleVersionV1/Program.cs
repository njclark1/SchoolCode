//programmer: nickj.clark14@gmail.com
//date: 12/7/2021

//imports
using System;

//namespaces
namespace Grader;

//program class
class Program
{
    //main function
    static void Main(string[] args)
    {
        //variables
        int numAnswersIncorrect = 0;
        //student answer array
        string[] studentArray;
        studentArray = new string[20];

        //correct answer array
        string[] correctArray;
        correctArray = new string[20];

        //introduce program to user
        Console.WriteLine("Hello, this program will grade your exam");

        //call function to read student answer file
        readStudentFile(studentArray);
        testPrintArray(studentArray);


        //call function to read correct answer file
        readCorrectFile(correctArray);
        testPrintArray(correctArray);

        //call function to calculate the number of incorrect answers
        calcNumIncorrectAnswers(numAnswersIncorrect, studentArray, correctArray);

    }//end main function

    //function to parse student answer file
    static void readStudentFile(string[] studentArray)
    {
        //update user
        Console.WriteLine("reading student file to array");

        //variables
        string studentPath = "studentAnswers.txt";

        //read file
        if (File.Exists(studentPath))
        {
            //log if file found
            Console.WriteLine("\nFound student file\n");
            int counter = 0;

            // Read the file and display it line by line.  
            foreach (string line in File.ReadLines(studentPath))
            {
                studentArray[counter] = line;
                counter++;
            }
        }
    }//end readstudentfile

    //function to parse correct answer file
    static void readCorrectFile(string[] correctArray) {
        //update user
        Console.WriteLine("reading correct answer file to array");

        //variables
        string correctPath = "correctAnswers.txt";

        //read file
        if (File.Exists(correctPath))
        {
            //log if file found
            Console.WriteLine("\nFound correct answer file\n");
            int counter = 0;

            // Read the file and display it line by line.  
            foreach (string line in File.ReadLines(correctPath))
            {
                correctArray[counter] = line;
                counter++;
            }
        }
    }//end readcorrectfile

    //function to print chosen array to console
    static void testPrintArray(string[] printArray)
    {
        Console.WriteLine("\nprinting array chosen to test\n");
        int counter = 0;
        foreach (string line in printArray)
        {
            Console.WriteLine(line);
            counter++;
        }
    }//end testprint function

    //function to calculate the number of incorrect answers
    static void calcNumIncorrectAnswers(int numIncorrect, string[] studentArray, string[] correctArray)
    {
        Console.WriteLine("calculating number of incorrect answers");
    }//end calcincorrect function

    }//end program

