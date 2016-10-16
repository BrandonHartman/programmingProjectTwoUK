
Write a Python program that will display a message to ask the user to input the type of residency.
The program then reads the residency (‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate).
Based on the residency, the program will use the respective current tuition and respective word of
either UNDERGRADUATE or GRADUATE ... this needs an if ... elif ... else ....

The program will then enter a loop and calculate the new tuition for every year for five years and
inside the loop display a line of the table that will look as below, formatting output amounts to 2
decimal places for amounts.

Your program should have only one print( ) statement to produce all the five non-heading lines. This
is the whole purpose of a loop. Also, the word UNDERGRADUATE in the headings should be replaced by GRADUATE
when a ‘G’ is selected.
--------------------------------------------------------------------------------------------------------------------------
Problem Definition
At a certain college, the current tuition is as follows: RESIDENCY ANNUAL TUITION In-state undergraduate student’s tuition equals $10,000 per year. Out-of-state undergraduate student’s tuition equals $24,000 per year. Professional graduate student’s tuition equals $40,000 per year.  The tuition will be increased by 3% (0.03) every year for the next 5 years. Write a Python program that will display a message to ask the user to input the type of residency. The program then reads the residency (‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate). Based on the residency, the program will use the respective current tuition and respective word of either UNDERGRADUATE or GRADUATE … this needs an if … elif … else …. The program will then enter a loop and calculate the new tuition for every year for five years and inside the loop display a line of the table that will look as below, formatting output amounts to 2 decimal places for amounts. 

Analysis
We have picked Python as our language for this project because we are currently learning the programming language in class...I decided to start the program right away in a while loop. I did this statement because I wanted the loop to continue if the user accidentally entered a number or letter that was not assigned in the program. I set an error message for this scenario so that the program would not exit on the user. It will print an error message of “Invalid Input. Please try again.” And reset to the beginning of the loop until correct input is entered.

In the program, tuition is set till none while inside the loop until the input function asking what residency worked for you. After input, it will assign the input that the user picked as a variable. The program will go into an If-elif-else and state if tuition is equaled to “I”..  That inState equals to 10,000. Afterwards, tuition is equaled to inState. The last part is a print statement outputting “Undergraduate tuition for the next five years”. Running a elif, only if tuition is equaled to “0”. It will state that outOfState is equaled to 24,000. Afterwards, tuition is equaled to outOfState. The last part is a print statement outputting “Undergraduate tuition for the next five years”.
Running a elif, only if tuition is equaled to “G”. It will state that profGraduate is equaled to 40,000. Afterwards, tuition is equaled to profGraduate. The last part is a print statement outputting “Graduate tuition for the next five years”.

After the while loop and setting which variables are assigned to the user’s residency. The visual output that the user will see as the program begins. We will start with two print statements that are aligned “Academic Year”, “Tuition” and “Increase”. Also, below the last statement is
 “---------------” below the aligned titles. This states where the next variables will be aligned and printed after the loop extends to its max.

The next few paragraphs are the main functions of the program. It is where the variable loops 5 times to assign a new outcome each post. Moreover, the program will save the state of the start until the loop starts. So the program states a start, end and step within my_range to start the basic accumulator. The basic accumulator is to keep the tally of the academic years. First, by setting the line variable to 16 to make sure that the program will get “-17”,”-18”..etc. But to achieve this accumulator. The program will need a basic count variable equaled to 1. The accumulator is set within the program. The next state to follow is the “For” loop that states “For academicYears in my_range of 2016 through 2020. With a step count of 1. Under this loop, with “Indention”.. States that line is equaled to the equation of line plus count. Also, under that function stats through the academic years is where the formatting of range is set. On to the next variables of tuition and Increase variable. The program will set a variable named tuitionIncrease. Setting this variable will be taking the tuition value that is set at the beginning and multiplying it by three percent. One of the main rules for the project was to use the print function once by creating the loop. Here is the only print statement within the loop in the program. The program will format yearsThroughAcademics to the left aligned with its title that is aligned as a string. Tuition will be aligned 21 characters that is a “float and two decimal points in the middle of the program. Finally, tuitionIncrease will be aligned all the way to the right to be aligned with Increase. This will also be placed two decimal points and converted to float and 13 characters away. The selected with numbers will also have “,” to make the numbers generate correctly.

Finally, the ending of the visual output that the user will see when the program outputs it. The program will format “Total Tuition Increase” and the variable finalTuitionIncrease 20 character places (float) to align with increase. This variable will also be placed two decimal points with a “,” for its final number that is printed to the screen.

Design
Here is thePseudocode:
•	Tuition is equaled to none until assigned
•	Input “‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate
•	Assign Tuition to inState if user enters ‘I’
•	Tuition will equal to 10,000
•	Print “Undergraduate Tuition for The Next Years”
•	Assign Tuition to outOfState if user enters ‘O’
•	Tuition will equal to 24,000
•	Print “Undergraduate Tuition for The Next Years”
•	Assign Tuition to profGraduate if user enters ‘G’
•	Tuition will equal to 40,000
•	Print “Undergraduate Tuition for The Next Years”
•	Else print “Invalid Input. Please try again.”
•	Reprint the “‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate
•	State the range of the accumulator
•	State the start of the accumulator
•	State the end of the accumulator 
•	State the step of the accumulator
•	Save the state of the start accumulation
•	Create a variable assigned as line that is equaled to 16
•	Create a variable assigned as count that is equaled to 1.
•	State a loop that functions for academicYears in my_range.
•	The range is set for the Start, End and the Set 
•	Set to 2016, 2020, and 1.
•	Line equals to count plus line
•	Format the variable yearsThroughAcademics and Line.
•	Create a variable named tutionIncrease that is equaled to Tuition times 3 percent
•	Tuition is equaled to tuitionIncrease plus Tuition
•	Only print function to perform all statements in loop
•	Format yearsThroughAcademics aligned to Acadmeic Years
•	Format tuition 21 characters and a float. 
•	Also, 2 decimal points for tuition
•	Format tuitionIncrease 13 character spaces and align to float.
•	Also, 2 decimal points for tuitionIncrease.
•	Final ending part of the program formats and prints the total tuition
•	finalTuitionIncrease is assigned to equal tuition multiplying be the interest of .159274
•	That states the interest over five years.
•	Run the program and receive the final total amount.
•	

Implementation
The development environment used for this program was PyCharm CE. I programmed it on my Mac pro using the OS Operating System. I had a couple unusual situations happen while developing this program. I ran into a problem with the For loop. I could print the tuition an Increase that was wanted. However, the Academic Years loop was quite the problem. Getting the -17, -18..etc was the issue. I had to set a base counting loop to control it. After hours of pulling my hair out…I Finally got the right output and celebrated until I tried to improve it and yet another syntax error…BUT ERRORS ARE MY FRIENDS and the HELP!
