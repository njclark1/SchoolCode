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

        //call function to read student answer file
        readStudentFile();

        //call function to write student answers to array 
        Console.WriteLine("\nwriting student answers to array\n");
        writeStudentArray();

        //call function to read correct answer file
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
            //log if file found
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
            //log if file found
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

    //function to write student answers to array
    public static Array[] writeStudentArray()
    {
        //variables
        Array[] studentArray;
        studentArray = new Array[20];

        //loop to write array
        for (int i = 0; i < studentArray.Length; i++)
        {
            Console.WriteLine("test");
        }
        //return array
        return studentArray;
    }//end function to write student answers to array

}//end program

