"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

###--- IMPORTS ---###
import csv
import re

###--- GLOBAL VARIABLES ---###
regex = r"[\s+\(|\)]"


###--- CODE ---###
def get_unique_phone_numbers():
    '''
     opens and reads texts.csv
     opens and reads calls.csv
     creates a list of unique phone numbers
     prints out final count in expected format
    '''

    f = open('texts.csv', 'r')
    reader = csv.reader(f)
    texts = list(reader)

    unique_phone_numbers = list()

    for row in texts:
        text_sender = re.sub(regex, '', row[0].lstrip('0'))

        if text_sender not in unique_phone_numbers:
            unique_phone_numbers.append(text_sender)

        text_recipient = re.sub(regex, '', row[1].lstrip('0'))

        if text_recipient not in unique_phone_numbers:
            unique_phone_numbers.append(text_recipient)

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    for row in calls:
        caller = re.sub(regex, '', row[0].lstrip('0'))

        if caller not in unique_phone_numbers:
            unique_phone_numbers.append(caller)

        call_recipient = re.sub(regex, '', row[1].lstrip('0'))

        if call_recipient not in unique_phone_numbers:
            unique_phone_numbers.append(call_recipient)

    print(
        f"There are {len(unique_phone_numbers)}"
        " different telephone numbers in the records.")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    get_unique_phone_numbers()
