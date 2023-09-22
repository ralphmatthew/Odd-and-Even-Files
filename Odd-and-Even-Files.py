#This code appends the user's text file and writes two separate files (odd and even) from it. 
#The first file will contain all odd numbers from the user's file and the second file contains even numbers.
#The user should have a text (.tx) file named "numbers" containing integers in order for the code to be read.

with open("numbers.txt") as a:
    numbers = [int(x) for x in a.read().split()]

with open("odd.txt", "w") as a:
    for num in numbers:
        if num % 2 == 1:
            a.write(str(num) + "\n")

with open("even.txt", "w") as a:
    for num in numbers:
        if num % 2 == 0:
            a.write(str(num) + "\n")
