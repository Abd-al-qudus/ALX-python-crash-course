#Python Assignment
#Mentor:	Qudus IBN					@24.11.23

Python Conditional Statements
Conditional statements, also known as decision-making statements, are used to control the flow of a program based on certain conditions. They allow you to make decisions based on the values of variables or the results of expressions. Python supports various conditional statements, including if, elif, else, and switch.

if Statement
The if statement is the most basic form of a conditional statement. It evaluates a condition and executes a block of code if the condition is true. The syntax of the if statement is:

Python
if condition:
    # code to execute if condition is true
Use code with caution. Learn more
For example, the following code checks if a number is equal to 10:

Python
num = 10
if num == 10:
    print("The number is equal to 10")
Use code with caution. Learn more
if-else Statement
The if-else statement is used to execute different blocks of code based on whether a condition is true or false. The syntax of the if-else statement is:

Python
if condition:
    # code to execute if condition is true

else:
    # code to execute if condition is false

Use code with caution. Learn more
For example, the following code checks if a number is positive or negative:

Python
num = -5
if num > 0:
    print("The number is positive")
else:
    print("The number is negative or zero")
Use code with caution. Learn more
if-elif-else Statement
The if-elif-else statement allows you to check multiple conditions and execute different blocks of code based on the outcome of each condition. The syntax of the if-elif-else statement is:

Python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
elif condition3:
    # code to execute if condition3 is true
...
else:
    # code to execute if none of the conditions are true
Use code with caution. Learn more
For example, the following code checks if a grade is an A, B, C, D, or F:

Python
grade = "A"
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Very good")
elif grade == "C":
    print("Good")
elif grade == "D":
    print("Pass")
else:
    print("Fail")
Use code with caution. Learn more
switch Statement
The switch statement is an alternative to using nested if-elif statements for multiple conditions. It allows you to specify a set of values and associated code blocks. The syntax of the switch statement is:

Python
switch (variable):
    case value1:
        # code to execute for value1
    case value2:
        # code to execute for value2
    case value3:
        # code to execute for value3
    ...
    default:
        # code to execute if none of the cases match
Use code with caution. Learn more
For example, the following code checks the day of the week:

Python
day = "Wednesday"
switch (day):
    case "Monday":
        print("It's Monday")
    case "Tuesday":
        print("It's Tuesday")
    case "Wednesday":
        print("It's Wednesday")
    case "Thursday":
        print("It's Thursday")
    case "Friday":
        print("It's Friday")
    case "Saturday":
        print("It's Saturday")
    case "Sunday":
        print("It's Sunday")
    default:
        print("Invalid day")
Use code with caution. Learn more
Conclusion
Conditional statements are essential for writing complex and flexible programs. They allow you to control the flow of your code based on various conditions, making your programs more responsive and adaptable.
