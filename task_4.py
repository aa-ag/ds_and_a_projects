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


###--- CODE ---###
def identify_possible_telemarketers():
    '''
     open & read calls.csv, as well as texts.csv
     create a set of possible telemarketers.
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

    numbers_that_received_incoming_calls = set()
    answer = set()

    for row in calls:
        numbers_that_received_incoming_calls.add(row[1])

        if row[0] not in numbers_that_received_incoming_calls and \
            row[0] not in texts[0] and \
                row[0] not in texts[1]:
            answer.add(row[0])

    # The list of numbers should be print out one per line
    # in lexicographic order with no duplicates.

    print("These numbers could be telemarketers:")

    for potential_telemarketer in sorted(list(answer)):
        print(potential_telemarketer)


###--- DRIVER CODE ---###
if __name__ == '__main__':
    identify_possible_telemarketers()
