# Author: Norman C Blizard
# Date: 11/3/2026
# revised 11/8/2026 : changed case of quit test to 'ZZZ' and forced uppercase, added else/print
# file name: Module2_GPAcalculator3.py
# URL: https://github.com/normc812/Module-2-IfElse/blob/main/Module2_GPAcalculator3.py
#
#Description: This program inputs the 
# last and first names and GPA
# of a student and determines whether they are 
# on the Deans List or Honor Roll.  
#
# variables: 
# GPA - the GPA of the student
# student_first - first name of the student
# student_last - the last name of the student
# 
# Note: based on peer review, I made a change to the signal value to quit and now case insensitive, 
# and added a print if student did not qualify for either list
#

while True:  # this infinite loop will continue until the user enters "ZZZ" to quit
    #
    student_last= input("Enter the student's last name, ZZZ to quit: ") 
    if student_last.upper() == "ZZZ": # ZZZ is the value to quit the program, made input case insensitive
        break
    student_first = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    if GPA >= 3.5:
        print(student_first.capitalize() + " " + student_last.capitalize(), "is on the Dean's List.")
    elif GPA >= 3.25:
        print(student_first.capitalize() + " " + student_last.capitalize(), "is on the Honor Roll.")
    else:
         print(student_first.capitalize() + " " + student_last.capitalize(), "is not on Dean's List" 
              " or Honor Roll")   # added this final else/print lines from peer review feedback


print("Thank you for using the GPA calculator version 3.")
   
    
    
