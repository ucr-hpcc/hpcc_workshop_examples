#!/bin/bash

# top500_example_bash.sh

# This script reads the TOP500 supercomputer rankings, and outputs smaller
# tables by filtering by country.
# Bash, along with standard Unix programs, can be used for basic text
# processing. However, other languages like Perl, Python, and R should be
# considered for anything non-trivial.

# Variables that the user might want to customize should be placed on the top
# and clearly named. Hard-coding such details will likely cause problems later.

# This directive tells Bash to stop execution at any (uncaught) error.
# Otherwise, Bash would continue execution, which could cause a further cascade
# of problems and make it more difficult to investigate.
set -e

# Tab-separated file to read
INPUT_FILE="TOP500_202211_trimmed.csv"

# Output prefix for output files
# Consider starting the prefix with a different letter than the input, so you
# can easily delete output files with a wildcard (rm out*)
OUTPUT_PREFIX="out_top500_"

# List (array) of countries to filter
COUNTRIES=("China" "Germany" "United States")

# Bash does a lot of word-splitting on its own. This is great for interpreting
# commands on a terminal, but infuriating for text processing.
# The "IFS" variable governs its behavior. We set it here to only split at
# new lines.
IFS=$'\n'

# INDEXES is an associative array that will be used to more clearly express
# which column index we're trying to target.

declare -A INDEXES

INDEXES[Rank]=1
INDEXES[Name]=2
INDEXES[Computer]=3
INDEXES[Site]=4
INDEXES[Manufacturer]=5
INDEXES[Country]=6
INDEXES[Processor]=11

# Helper function to gather info on a country's top supercomputer (located
# at the second row of its output file.)
# Usage: get_top_info COUNTRY_FILE COLUMN_INDEX

get_top_info() {
    echo $(head -n 2 "$1" | tail -n 1 | cut -f "$2")
}

# "tr" is a simple tool that "translates" one string with another.
# It is used here to replace spaces in the country name so that no spaces are
# added to the output file name.

# "head" and "tail" are tools to quickly view the top and bottom of a file
# respectively. By adjusting the range with "-n", we can extract only the parts
# of the input file we want (e.g. ignore header lines)

# "cut" is a tool to isolate certain parts of a line in a file.
# We use it to obtain specific columns in a line of data. By default, "cut"
# separates parts by TAB.

# "wc" is a word counting tool.
# In this example, we are counting by line, rather than by individual words.
# This can be useful for counting how many records a line-based file has.

# "awk" is a text manipulation tool.
# It is actually a full programming language on its own right, but you'll often
# see it used in a similar way as "cut".

# Filter the input file once for each country in the list.
# In practice, it's better to read the file in one pass and incrementally
# append results to the corresponding output file.

for C in "${COUNTRIES[@]}"; do
    # Create a name for the output file. Replace spaces with underscore.
    C1=$(echo "$C" | tr ' ' '_')
    OUTPUT_FILE="$OUTPUT_PREFIX$C1.csv"

    # Remove any existing file and initialize a new file with a header.
    rm -f "$OUTPUT_FILE"
    head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"

    # Loop through all lines/rows starting from the 2nd.
    for line in $(tail -n +2 $INPUT_FILE); do
        # Get the country's name from the line and compare it with the
        # country being processed in the outer loop.
        C2=$(echo $line | cut -f ${INDEXES[Country]})
        if [ "$C" == "$C2" ]; then
            # If they're the same, write the line to the output file.
            echo $line >> "$OUTPUT_FILE"
        fi
    done

    # Count how many supercomputers were found in this country.
    # Subtract 1 for the top (header) row
    NUM=$(wc -l "$OUTPUT_FILE" | awk '{print $1}')
    NUM=$(( $NUM-1 ))

    # Output results.
    echo "$C has $NUM supercomputers in the TOP500"
    TOP_RANK=$(get_top_info "$OUTPUT_FILE" ${INDEXES[Rank]})
    TOP_NAME=$(get_top_info "$OUTPUT_FILE" ${INDEXES[Name]})
    TOP_SITE=$(get_top_info "$OUTPUT_FILE" ${INDEXES[Site]})
    echo "It's top supercomputer is ranked number $TOP_RANK, is known as $TOP_NAME, and is located at $TOP_SITE."
done
