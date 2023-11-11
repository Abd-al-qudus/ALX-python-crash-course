#Python Assignment
#Mentor:	Qudus IBN					@11.11.23

This assignment covers the following basic Python topics:

#!/usr/bin/python3
print()
fast print
slice variables
split()
#!/usr/bin/python3

This line is called a shebang, and it tells the operating system which interpreter to use to run the script. In this case, we are telling the operating system to use the Python 3 interpreter.

print()

The print() function is used to print output to the console. For example, the following code will print the string "Hello, world!" to the console:

Python
print("Hello, world!")
Use code with caution. Learn more
fast print

The fast print function is a more efficient way to print output to the console than the print() function. However, it is not as well-supported by all Python interpreters.

To use the fast print function, you can use the following syntax:

#Python
print(*objects, sep=" ", end="\n")
Use code with caution. Learn more
The *objects argument is a sequence of objects that you want to print. The sep argument is a string that is used to separate the objects when they are printed. The end argument is a string that is printed at the end of the output.

For example, the following code will print the strings "Hello" and "world!" to the console, separated by a space:

#Python
print(*["Hello", "world!"], sep=" ")
Use code with caution. Learn more
slice variables

Slice variables are used to select a subset of a sequence, such as a string or a list. To slice a variable, you use the following syntax:

#Python
variable[start:end:step]
Use code with caution. Learn more
The start argument is the index of the first element that you want to select. The end argument is the index of the last element that you want to select, but it is not included in the slice. The step argument is the interval at which you want to select elements. If you omit the step argument, it will default to 1.

For example, the following code will select the first three characters of a string:

Python
string = "Hello, world!"
sliced_string = string[:3]

print(sliced_string)
Use code with caution. Learn more
Output:

Hel
split()

"""The split() method is used to split a string into a list of strings. The split() method takes a separator as an argument, and it splits the string at every occurrence of the separator."""

For example, the following code will split the string "Hello, world!" at the space character:

Python
string = "Hello, world!"
split_string = string.split(" ")

print(split_string)
Use code with caution. Learn more
Output:

['Hello', ',', 'world!']
Assignment

For your assignment, you will write a Python script that uses all of the concepts covered in this README file. Your script should do the following:

Prompt the user for a string.
Print the string to the console using the fast print function.
Select the first three characters of the string using a slice variable.
Split the string into a list of words using the split() method.
Print the list of words to the console.
Example Output

Enter a string: Hello, world!

Hello, world!
Hel
['Hello', ',', 'world!']
