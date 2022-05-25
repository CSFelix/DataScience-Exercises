#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    # Function to sort the List Map bellow by n_chars
    def sort_by_n_chars(map): return map['n_chars']

    # List Map containing {'n_chars' : int, 'text' : String}
    top_10 = []

    for line in reader:
        top_10.append({'n_chars' : len(line[4]), 'text' : line})
    
    # Sorting the List Map and dropping the shortest text
    top_10.sort(key=sort_by_n_chars)
    top_10.remove(top_10[0])


    # Printing the texts from
    # the shortest one to the longest
    for element in top_10: writer.writerow(element['text'])

# Testing the Algorithm
test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    #import StringIO
    #sys.stdin = StringIO.StringIO(test_text)

    import io
    sys.stdin = io.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

main()