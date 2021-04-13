"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

###--- IMPORTS ---###
import csv


###--- CODE ---###
def count_unique_phone_numbers():
    '''
     opens and reads texts.csv
     opens and reads calls.csv
     creates a list of unique phone numbers
     prints out final count in expected format
    '''

    f = open('texts.csv', 'r')
    reader = csv.reader(f)
    texts = list(reader)

    unique_phone_numbers = set()

    for row in texts:
        unique_phone_numbers.add(row[0])
        unique_phone_numbers.add(row[1])

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    for row in calls:
        unique_phone_numbers.add(row[0])
        unique_phone_numbers.add(row[1])

    print(
        f"There are {len(unique_phone_numbers)}"
        " different telephone numbers in the records.")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    count_unique_phone_numbers()
