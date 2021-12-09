//programmer: nickj.clark14@gmail.com
//date: 12/7/2021

//prompt
/*Write a program that reads the contents of a text file with these answers, then reads the contents of 
another file containing the student answers, and then compares the two answers (hint: character arrays 
may be helpful here). The program should then determine the number of questions that the student 
missed, and then display the following:

DONE - A list of the questions missed by the student, showing the correct answer and the incorrect 
answer provided by the student for each missed question.

DONE - The total number of questions missed.

DONE - The percentage of questions answered correctly. This can be calculated as Correctly Answered 
Questions / Total Number of Questions.

DONE - If the percentage of correctly answered questions is 70 percent or greater, the program should 
indicate that the student passed the exam. Otherwise, it should indicate that the student failed 
the exam.
*/
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
        Console.WriteLine("Hello! This program will grade your exam\n");

        //call function to read student answer file
        readStudentFile(studentArray);
       // testPrintArray(studentArray);


        //call function to read correct answer file
        readCorrectFile(correctArray);
       // testPrintArray(correctArray);

        //call function to calculate the number of incorrect answers
        numAnswersIncorrect = calcNumIncorrectAnswers(studentArray, correctArray);
        Console.WriteLine("\nThe number of answers this student has missed is: " + numAnswersIncorrect);

        //call function to calculate total grade
        calcResults(numAnswersIncorrect);
    }//end main function

    //function to parse student answer file
    static void readStudentFile(string[] studentArray)
    {
        //variables
        string studentPath = "studentAnswers.txt";

        //read file
        if (File.Exists(studentPath))
        {
            //variables
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

        //variables
        string correctPath = "correctAnswers.txt";

        //read file
        if (File.Exists(correctPath))
        {
            //variables
            int counter = 0;

            // Read the file and display it line by line.  
            foreach (string line in File.ReadLines(correctPath))
            {
                correctArray[counter] = line;
                counter++;
            }
        }
    }//end readcorrectfile

    //function to calculate the number of incorrect answers
    static int calcNumIncorrectAnswers(string[] studentArray, string[] correctArray)
    {
        //update user
        Console.WriteLine("#Calculating incorrect answers\n");

        //variables
        int numIncorrect = 0;
        int counter = 0;

        //count number of lines that aren't the same
        foreach (string line in studentArray)
        {
            if (studentArray[counter] != correctArray[counter])
            {
                numIncorrect++;
                Console.WriteLine("Student missed question# " + counter + ". \nThe incorrect answer given was: " + line + "\nThe correct answer was: " + correctArray[counter]);
            }
            counter++;
        }
        return numIncorrect;
    }//end calcincorrect 

    static void calcResults(int numIncorrect)
    {
        //variables
        int numQuestions = 20;
        int numCorrect = numQuestions - numIncorrect;
        double gradePercentage = (double)numCorrect / (double)numQuestions;
        gradePercentage = gradePercentage * 100;
        bool passed = true;

        if (gradePercentage >= 70)
        {
            passed = true;
        }
        else
        {
            passed = false;
        }

        //output results to user
        Console.WriteLine("The student's percentage grade is: " + gradePercentage + "%");
        if (passed == true)
        {
            Console.WriteLine("\nHooray! This student has passed the test");
            
        }
        else
        {
            Console.WriteLine("\nUnfortunately, this student has not passed the test");
        }

        //function to print chosen array to console
        //unused at the moment, but possibly useful for debugging
        /*
            static void testPrintArray(string[] printArray)
            {
                Console.WriteLine("\n#Printing array chosen to test\n");
                int counter = 0;
                foreach (string line in printArray)
                {
                    Console.WriteLine(line);
                    counter++;
                }
            }//end testprint function
        */
    }

}//end program

