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
def unique_phone_numbers():
    '''
     opens and reads texts.csv
     opens and reads calls.csv
     creates a list of unique phone numbers
     prints out final count in expected format
    '''
    global regex

    unique_phone_numbers = list()

    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    for row in texts:

        from_number = re.sub(regex, '', str(row[0].lstrip('0')))

        if from_number not in unique_phone_numbers:
            unique_phone_numbers.append(from_number)

        to_number = re.sub(regex, '', str(row[1].lstrip('0')))

        if to_number not in unique_phone_numbers:
            unique_phone_numbers.append(to_number)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    for row in calls:
        from_number = re.sub(regex, '', str(row[0].lstrip('0')))

        if from_number not in unique_phone_numbers:
            unique_phone_numbers.append(from_number)

        to_number = re.sub(regex, '', str(row[1].lstrip('0')))

        if to_number not in unique_phone_numbers:
            unique_phone_numbers.append(to_number)

    print(
        f"There are {len(unique_phone_numbers)}"
        " different telephone numbers in the records.")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    unique_phone_numbers()
