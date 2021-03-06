"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

###--- IMPORTS ---###
import csv


###--- CODE ---###
def longest_time_on_the_phone():
    '''
     opens and reads texts.csv
     opens and reads calls.csv
     creates a list of phone call lenghts, in seconds
     prints out phone number of longest call in expected format
    '''
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    print(f"{} spent the longest time, {} seconds, on the phone during")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    longest_time_on_the_phone()
