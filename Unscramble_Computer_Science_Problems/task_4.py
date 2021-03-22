"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

###--- IMPORTS ---###
import csv
import re


###--- GLOBAL VARIABLES ---###
regex = r"[\s+\(|\)]"


###--- CODE ---###
def identify_possible_telemarketers():
    '''
     open & read calls.csv, as well as texts.csv
     create a list of possible telemarketers.
     these numbers:
     (i) make outgoing calls
     (ii) never receive incoming calls, 
     (iii) never receive texts, or  
     (iv) never send texts.
    '''

    f = open('texts.csv', 'r')
    reader = csv.reader(f)
    texts = list(reader)

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    numbers_that_received_incoming_calls = list()

    for row in calls:
        if row[1] not in numbers_that_received_incoming_calls:
            numbers_that_received_incoming_calls.append(row[1])

    # The list of numbers should be print out one per line
    # in lexicographic order with no duplicates.
    answer_list = list()

    for row in calls:
        if row[0] not in numbers_that_received_incoming_calls and \
            row[0] not in texts and \
                row[0] not in answer_list:
            answer_list.append(row[0])

    answer_string = "These numbers could be telemarketers: "
    print(answer_string)

    for potential_telemarketer in sorted(answer_list):
        print(re.sub(regex, '', potential_telemarketer))


###--- DRIVER CODE ---###
if __name__ == '__main__':
    identify_possible_telemarketers()
