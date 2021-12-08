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
        //introduce program to user
        Console.WriteLine("Hello, this program will grade your exam");

        //call functiton to read student answer file
        readStudentFile();        
        
        //call functiton to read correct answer file
        readCorrectFile();

    }//end main function

    //function to parse student answer file
    static void readStudentFile()
    {
        //variables
        string studentPath = "studentAnswers.txt";

        //read file
        if (File.Exists(studentPath))
        {

            Console.WriteLine("\nFound student file\n");
            int counter = 0;

            // Read the file and display it line by line.  
            foreach (string line in File.ReadLines(studentPath))
            {
                Console.WriteLine(line);
                counter++;
            }
        }
    }//end readstudentfile

    //function to parse correct answer file
    static void readCorrectFile() { 

        //variables
        string correctPath = "correctAnswers.txt";

        //read file
        if (File.Exists(correctPath))
        {

            Console.WriteLine("\nFound correct answer file\n");
            int counter = 0;

            // Read the file and display it line by line.  
            foreach (string line in File.ReadLines(correctPath))
            {
                Console.WriteLine(line);
                counter++;
            }
        }
    }//end readcorrectfile
}//end program
