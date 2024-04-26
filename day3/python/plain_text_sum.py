#!/usr/bin/env python3

## This script is a simple demonstration of parsing a text file.
## It expects a text file with integers, separated by spaces.
## This script then prints the sum of all numbers for each line.
## Such a source file can be generated with the following Bash code:

# for i in {1..10}; do
#   for j in {1..5}; do
#     echo -n $((RANDOM % 100)) ' ' >> random_5x10.txt
#   done
#   echo '' >> random_5x10.txt
# done

# Input file
INPUT_FILE = "random_5x10.txt"

# Open a file for reading
f = open(INPUT_FILE, "r")

# Initialize the linestr variable for the while loop
linestr = f.readline()

# readline() returns an empty string on end-of-file
while linestr != '':
    # Because the input file is text, we need to clean it up and force Python
    # to interpret the strings as integers.
    # linestr.strip() removes extra spaces from the sides of the string.
    # .split() then separates the string into a list.
    # int(x) forces the conversion of the string into an integer
    # The syntax [ f(x) for x in LIST ] is known as "list comprehension", and
    # is a compact way to transform one list to another.
    numlist = [ int(x) for x in linestr.strip().split() ]

    # Print the sum (sum() is a built-in Python function)
    print(sum(numlist))

    # Prepare linestr for the next loop.
    # BEWARE! Forgetting this step is a common programming mistake!
    # Your code will loop forever if you forget this!
    linestr = f.readline()

# Close the file when you're done
f.close()
