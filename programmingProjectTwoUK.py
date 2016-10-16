# Programming Project Two
# Brandon Hartman
# October 7th, 2016
# -----------------------------------------------------------------------------

# Write a Python program that will display a message to ask the user to
# input the type of residency. The program then reads the residency
# (‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate).
# Based on the residency, the program will use the respective current tuition
# and respective word of either UNDERGRADUATE or GRADUATE … this needs an
# if … elif … else ….

# The program will then enter a loop and calculate the new tuition for every
# year for five years and inside the loop display a line of the table that
# will look as below, formatting output amounts to 2 decimal places for amounts.

# Tuition will be increased by 3% (0.03) every year for the next 5 years.

# Your program should have only one print( ) statement to produce all the five
# non-heading lines. This is the whole purpose of a loop. Also, the word
# UNDERGRADUATE in the headings should be replaced by GRADUATE when a ‘G’
# is selected.
# -----------------------------------------------------------------------------

# We will be asking the user for input and assigning it to the tuition variable.
# This action states three different types of assignments that it can go into.
# These assignments are inState, outOfState and profGraduate.
# At the moment, tuition is set to None until further assignment.
tuition = None

# The user will will enter which residency aligns with them.
# 'I' for inState. 'O' for outOfState. 'G' for profGraduate.
# After user enters their input..It will go into a while loop and follow by
# if-elif-else statement. This next section goes into a while loop and will run until
# tuition is set to something.

# The program will state that if tuition is equal to I in the user input that..
# tuition is equal to inState.
# inState is assigned to the tuition amount of 10,000.
# The program will print either Undergraduate or Graduate depending on the user.
# In this case, inState and outOfState are Undergraduate.
# So it will print "UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS". The heading of the program.
while tuition is None:
    tuition = input("‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate.""\n")

    if tuition == "I":
        inState = 10000
        tuition = inState
        print("UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS")

    # The program will state that elif tuition is equal to O in the user input that..
    # That tuition is equal to outOfState.
    # outOfState is assigned to the tuition amount of 24,000.
    # The program will print either Undergraduate or Graduate depending on the user.
    # In this case, inState and outOfState are Undergraduate.
    # So it will print "UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS". The heading of the program.
    elif tuition == "O":
        outOfState = 24000
        tuition = outOfState
        print("UNDERGRADUATE TUITION FOR THE NEXT FIVE YEARS")

    # The program will state that elif tuition is equal to G in the user input that..
    # tuition is equal to profGraduate.
    # profGraduate is assigned to the tuition amount of 40,000.
    # The program will print either Undergraduate or Graduate depending on the user.
    # In this case, profGraduate is consider graduate.
    # So it will print "GRADUATE" TUITION FOR THE NEXT FIVE YEARS". The heading of the program.
    elif tuition == "G":
        profGraduate = 40000
        tuition = profGraduate
        print("GRADUATE TUITION FOR THE NEXT FIVE YEARS")

    # The finally section of this loop is the Else statement. If the user enters something besides
    # 'I', 'O' or 'G'..It will give an invalid message. (ERROR MESSAGE). It will send you back to the prompt
    # of asking for input.
    else:
        print("Invalid Input. Please try again. ")
        tuition = input("‘I’ for in-state, ‘O’ for out-of-state, and ‘G’ for graduate.")
# The program will start on the visual part of project. These next two print statements
# Are the headers of the visual part of the project. This header will show where "Academic
# Year", "Tuition" and "Increase" will be formatted and aligned.
print("ACADEMIC YEAR          TUITON      INCREASE")
print("-------------        --------    ----------")

# Total interest over five years. This will be the ending statement of the
# that will be printed and formatted at the end of the program.
finalTuitionIncrease = tuition * .159274

# The next set of functions will be the while loop to create the numbers for
# The academic years. However, this will not be the time that will output it
# To the screen. Moreover, we will save the state of the start until it is
# Called in the For loop below. More on the "Range" and start, end, step..This
# Will state that the starting point is 2016 and the end is 2020. Finally, the
# the step value will be 1. Again, the yield is to save the state of the start
# function.


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

# We will need to start a basic accumulator to keep the tally of the academic
# Years. First, set line to 16. to make sure that we will get -17, -18..etc.
# But to achieve this..We will need a basic count of 1.
line = 16
count = 1

# Accumulator is set. This next state will be the For Loop...
# For academicYears in the range of 2016 through 2020..
# Create a line following the next year. Making sure that all dates are updated
# within this loop by one.
for academicYears in my_range(2016, 2020, 1):
    line += count
    yearsThroughAcademics = "{0}-{1}".format(academicYears, line)

# That covers the Academic Year section..On to Tuition and Increase..
# We will need to set a variable named tuitionIncrease. Setting this variable
# will be taking the tuition value that is set at the beginning and multiplying
# it by three percent.

    tuitionIncrease = tuition * 0.03
    tuition += tuitionIncrease

# The finalTuitionIncrease will be set by multiplying 4 by tuitionIncrease
# To get the finally statement of the increase tuition.

# One of the main rules for the project was to use the print function once
# by creating the loop. Here is our only print statement within our loop.
# The program will format yearsThroughAcademics to the left aligned with its
# Title. Tuition will be aligned 21 characters and 2 decimal points right in
# middle of the program. Finally, tuitionIncrease will be aligned all the way
# to the right to be aligned with Increase. This will also be place two decimal
# points. The selected with numbers will also have "," to make the numbers.
    print(format(yearsThroughAcademics, "<0s"),
          format(tuition, ">21,.2f"),
          format(tuitionIncrease, ">13,.2f"))

# Finally, the ending of the visual output that the user will see.
# The program will format "TOTAL TUITION INCREASE" and the variable final
# TuitionIncrease 20 character places to align with increase. This variable
# will also be placed two decimal points and with a "," for it's final number.
print(format("TOTAL TUITION INCREASE"),
      format(finalTuitionIncrease, ">20,.2f"))
