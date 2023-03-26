#!/usr/bin/env python3

# top500_example_python.py

# This script does a simple tally of how many supercomputers each country has,
# based on the TOP500 rankings.
# This script does a bit more than top500_example_bash.sh, since we can
# leverage Python's additional features.

# The CSV (Character-Separated Values) library helps us parse the TOP500 file.
import csv

# By convention, variables with all-capital names should be treated as constant.
INPUT_FILE = "TOP500_202211_trimmed.csv"

# We provide these two constants for better readability. Otherwise anyone
# reading this code would have to remember the order of items in the tuple.
COUNTRY_IDX = 0
COUNT_IDX = 1

# Function example
# This function combines the names of countries if they have the same number
# of supercomputers. It assumes the provided list has already been sorted.

def combine_country_lines(in_list):
    # out_list is the data we will return at the end.
    # It has the same data as in_list, except that the country names will be
    # combined into a single item when the count is the same.
    out_list = list()

    for cur_tuple in in_list:
        if len(out_list) == 0:
            # First item. Just append it to the empty out_list
            out_list.append(cur_tuple)
        else:
            # Subsequent items, we compare the current count with the previous.
            # If they're the same, join the names of the two countries with a
            # comma separator.
            # Finally, replace the item in question with the updated country
            # string.
            prev_count = out_list[-1][COUNT_IDX]
            prev_country = out_list[-1][COUNTRY_IDX]
            if cur_tuple[COUNT_IDX] == prev_count:
                combined_name = ", ".join([prev_country, cur_tuple[COUNTRY_IDX]])
                out_list[-1] = (combined_name, prev_count)
            else:
                out_list.append(cur_tuple)

    return out_list

# Open the CSV file and load information into top500_list
# csv.DictReader considers the first row to contain the field names, and uses
# that name as the key when adding values to the resulting dict object.
top500_list = []
with open(INPUT_FILE, newline='') as f:
    dr = csv.DictReader(f, delimiter='\t')
    for row in dr:
        top500_list.append(row)

# These variables will be used as tallies
countries = dict()
cpu_maker = {
    "AMD": 0,
    "Fujitsu": 0,
    "IBM": 0,
    "Intel": 0,
    "Other": 0
}

# Perform the actual tally
for row in top500_list:
    country = row['Country']
    cpu_model = row['Processor']

    if row['Country'] not in countries:
        # If this is first appearance of a country, we must initialize its value
        countries[country] = 1
    else:
        # Otherwise, just increment its value
        countries[country] += 1

    # The TOP500 list doesn't have a dedicated column for CPU manufacturer,
    # so we need to tally based on keywords.
    if 'AMD' in cpu_model:
        cpu_maker['AMD'] += 1
    elif 'A64FX' in cpu_model:
        cpu_maker['Fujitsu'] += 1
    elif 'IBM' in cpu_model:
        cpu_maker['IBM'] += 1
    elif 'Xeon' in cpu_model:
        cpu_maker['Intel'] += 1
    else:
        cpu_maker['Other'] += 1

# dict objects were not originally designed to be ordered. As such, we need to
# transfer that data to a list object, which can be easily sorted.
# In this case, it will be a list of 2-tuples, where the tuples are of the form:
# (country, count)
country_tuples = list()

for country, count in countries.items():
    country_tuples.append( (country, count) )

# Python provides built-in sorting for lists. In the first sort, we're sorting
# by the country name (first part of the tuple). In the second sort, we're
# sorting by the count number (second part of the tuple), and we're doing a
# reverse-order sort so that higher numbers come first.
# The lambda function in the second sort tells the sorting algorithm to only
# look at the second part of the tuple (remember that list and tuple indexes
# start at 0)
list.sort(country_tuples)
list.sort(country_tuples, key=lambda x: x[1], reverse=True)

# Call the combine_country_lines function and save it's result.
country_tuples_combined = combine_country_lines(country_tuples)

# Finally, output our results.
# "\t" is the escape sequence for TAB.
# The first f-string may be more readable with spaces added:
# f"{ c[COUNT_IDX] }   \t   { c[COUNTRY_IDX] }"
print("Number of TOP500 clusters by country:")
for c in country_tuples_combined:
    print(f"{c[COUNT_IDX]}\t{c[COUNTRY_IDX]}")
print("")

print("Number of TOP500 clusters by CPU manufacturer:")
for manu, count in cpu_maker.items():
    print(f"{count}\t{manu}")
