# Author: Norman C Blizard
# Date: 11/3/2026
#file name: Module2_GPAcalculator1.py
#URL: https://github.com/normc812/Module-2-IfElse/blob/main/Module2_GPAcalculator1.py
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
while True:  # this infinite loop will continue until the user enters "zzz" to quit
    #
    student_last= input("Enter the student's last name, zzz to quit: ") 
    if student_last == "zzz": # zzz is the keyword value to quit the program
        break
    student_first = input("Enter the student's first name: ")
    GPA = float(input("Enter the student's GPA: "))
    if GPA >= 3.5:
        print(student_first.capitalize() + " " + student_last.capitalize(), "is on the Dean's List.")
    elif GPA >= 3.25:
        print(student_first.capitalize() + " " + student_last.capitalize(), "is on the Honor Roll.")


print("Thank you for using the GPA calculator.")
   
    
    
