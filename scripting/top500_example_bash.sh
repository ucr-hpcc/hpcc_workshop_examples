#!/bin/bash

# top500_example_bash.sh

# This script does a simple tally of how many supercomputers each country has,
# based on the TOP500 rankings.
# Bash, along with standard Unix programs, can be used for basic text
# processing. However, other languages like Perl, Python, and R should be
# considered for anything non-trivial.

INPUT_FILE="TOP500_202211_trimmed.csv"

# List (array) of countries to tally
COUNTRIES=("China" "France" "Germany" "Japan" "United States")

# COUNTRY_COUNT is an associative array that keeps track of how many TOP500
# supercomputers that country has.

# RESULTS is the text output of our filter pipeline. It is the count followed by
# the country name.

declare -A COUNTRY_COUNT
RESULTS=""

# Filter the input file once for each country in the list
# In practice, it's better to read the file in one pass and increment the
# corresponding tally at each line. However, this method was chosen to
# demonstrate pipelines.

# "cut" is a tool to isolate certain parts of a line in a file.
# In this example, we are asking for the 6th part, which is the country name.
# By default, "cut" separates parts by TAB.

# "grep" is a pattern matching tool.
# In this example, we are including lines that match the country name.

# "wc" is a word counting tool.
# In this example, we are counting by line, rather than by individual words.
# This can be useful for counting how many records a line-based file has.

# We save our results in the RESULTS variable.
# "\t" is the TAB character, and "\n" is the newline character. These are
# properly called "escape sequences".

for C in "${COUNTRIES[@]}"; do
    COUNT=$(cut -f 6 "$INPUT_FILE" | grep "$C" | wc -l)
    COUNTRY_COUNT["$C"]=$COUNT
    RESULTS+="$COUNT\t$C\n"
done

# "echo" is used to print text to standard output.
# "-e" tells echo to properly interpret escape sequences.

# "sort" is a line-sorting tool.
# By default, "sort" does a character-by-character comparison of each line,
# which we do not want for this example. "-n" tells "sort" to interpret numbers
# properly. "-r" reverses the results so the highest number is at the top.

echo "Countries by number of TOP500 supercomputers:"
echo -e $RESULTS | sort -n -r
