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

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    # set of numbers that
    make_outgoing_calls = set()
    received_incoming_calls_or_sent_text_or_received_text = set()

    for call in calls:
        make_outgoing_calls.add(call[0])
        received_incoming_calls_or_sent_text_or_received_text.add(call[1])

    f = open('texts.csv', 'r')
    reader = csv.reader(f)
    texts = list(reader)

    # sent texts, and/or
    # received texts
    for text in texts:
        received_incoming_calls_or_sent_text_or_received_text.add(text[0])
        received_incoming_calls_or_sent_text_or_received_text.add(text[1])

    answer = set()

    for row in calls:
        # if number has made outgoing calls
        # and has not received incoming calls,
        # sent a text, nor received a text
        if row[0] in make_outgoing_calls \
                and row[0] not in received_incoming_calls_or_sent_text_or_received_text:
            answer.add(row[0])

    # the list of numbers should be print out one per line
    # in lexicographic order with no duplicates.

    print("These numbers could be telemarketers:")

    for potential_telemarketer in sorted(list(answer)):
        print(potential_telemarketer)


###--- DRIVER CODE ---###
if __name__ == '__main__':
    identify_possible_telemarketers()
