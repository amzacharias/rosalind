# This program is for rosalind.info/problems/ini5/

# This program will read a file and return a new file with only even-numbered
# lines. 

# Amanda Zacharias; April 26th, 2021

"""
Notes:
open() to access a file

f.read(n) to read the file as a string. n = number of bytes of data to read

f.readline() to read a single line
    every line except the last line terminates w/ a newline character. Use
    .strip() to remove the newline.
    every time you call .readline(), it takes the next line in the file
    
f.readlines() returns a list of every line in the file.
    you can use f.readlines()[2] to read the third line of the file object

You can also read lines by looping over the file object
    for line in f:
        print line

Can use line.split() to separate data if they don't use \n as a delimiter.
    default = whitespace

Can use .splitlines() to return a list of strings, breaking at line boundaries

To save a file, open in write mode.

f.write() to write the data to a file
    you need to convert your input to str format

You can also use a for loop to write a list of items one at a time
    for i in list:
        f.write(str(i) + '\n') #\n means every item will start with a new line

must use f.close() at the end!
"""

"""
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file.
Assume 1-based numbering of lines.
"""

f = open("rosalind_ini5.txt", "r")

fileList = f.readlines()

i = 0
evenList = []
while i < len(fileList):
    # Using == 1 instead of == 0 because we're using 1-based numbering of lines
    # but python uses 0-based numbering, so everything is off by one.
    # Thus, even = odd. 
    if i % 2 == 1:
        evenList.append(fileList[i])
        i = i + 1
    else:
        i = i + 1

f.close()

evenFile = open("EvenFile_ini5.txt", "w")
for i in evenList:
    evenFile.write(str(i))
evenFile.close()








