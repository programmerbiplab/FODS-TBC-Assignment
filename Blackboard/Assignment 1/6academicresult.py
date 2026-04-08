'''The program below takes input as number/marks in 5 subjects and
and calculate the average, the total percentages and
the academic division of the student based on their obtained percentage'''

#user inputs number of marks of five subjects
sub1=int(input("Enter the marks of first subject:"))
sub2=int(input("Enter the marks of second subject:"))
sub3=int(input("Enter the marks of third subject:"))
sub4=int(input("Enter the marks of fourth subject:"))
sub5=int(input("Enter the marks of fifth subject:"))

#for average calculation
average=(sub1+sub2+sub3+sub4+sub5)/5
print("The average percentage of the student is:", average)

#for academic division
if average>80:
    print("The student has obtained: DISTINCTION")
elif average>60:
    print("The student has obtained: FIRST DIVISION")
elif average>50:
    print("The student has obtained: SECOND DIVISION")
elif average>45:
    print("The student has obtained: THIRD DIVISION")
elif average<45:
    print("The student has: FAILED")

#by Biplab Prasad Gajurel 25024641