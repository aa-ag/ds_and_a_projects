"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

###--- IMPORTS ---###
import csv
import re

###--- GLOBAL VARIABLES ---###
regex = r"[\s+\(|\)]"


###--- CODE ---###
def first_record_of_texts():
    '''
     opens & reads texts.csv
     slices first record/first element in list
     returns first record from text.csv
     in expected format string
    '''

    f = open('texts.csv', 'r')
    reader = csv.reader(f)
    texts = list(reader)

    first_record = texts[0]

    from_number = re.sub(regex, '', first_record[0].lstrip('0'))
    to_number = re.sub(regex, '', first_record[1].lstrip('0'))
    text_time = first_record[2].split()[1]

    answer_as_expected = f"First record of texts, " \
        f"{from_number} texts {to_number} " \
        f"at time {text_time}"

    print(answer_as_expected)


def last_record_of_calls():
    '''
     opens calls.csv
     reads calls.csv
     returns first record from calls.csv
    '''

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    last_record = calls.pop()

    from_number = re.sub(regex, '', last_record[0].lstrip('0'))
    to_number = re.sub(regex, '', last_record[1].lstrip('0'))
    call_time = last_record[2].split()[1]

    answer_as_expected = f"Last record of calls, " \
        f"{from_number} calls {to_number} " \
        f"at time {call_time}"

    print(answer_as_expected)


###--- DRIVER CODE ---###
if __name__ == '__main__':
    first_record_of_texts()
    last_record_of_calls()
