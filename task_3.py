"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
	 codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
	 of the number to help readability. The prefix of a mobile number
	 is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
	 with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

###--- IMPORTS ---###
import csv
import re


###--- GLOBAL VARIABLES ---###
regex = r"(080)"


###--- CODE ---###
def part_a():
    '''
    open & read calls.csv 
    use regular expression to check if number is from Bangalore
    if it is, add to answer in expected format 
    then print that answer
    '''
    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    call_recipients_called_by_a_number_from_bangalore = list()

    if regex in calls[6][0]:
        print(calls[6][1].split()[0])

    # expected_answer_format = "The numbers called by" \
    #     " people in Bangalore have codes: {}"


###--- DRIVER CODE ---###
if __name__ == '__main__':
    part_a()
