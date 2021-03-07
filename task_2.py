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
import re

###--- GLOBAL VARIABLES ---###
regex = r"[\s+\(|\)]"


###--- CODE ---###
def longest_time_on_the_phone():
    '''
     opens and reads texts.csv
     opens and reads calls.csv
     creates a list of phone call lenghts, in seconds
     prints out phone number of longest call in expected format
    '''
    global regex

    with open('calls.csv', 'r') as f:
        reader = csv.reader(f)
        calls = list(reader)

    time_on_phone_by_number = dict()

    for row in calls:

        from_number = re.sub(regex, '', str(row[0]))
        to_number = re.sub(regex, '', str(row[1]))
        duration = int(row[3])

        if from_number in time_on_phone_by_number:
            time_on_phone_by_number[from_number] += duration
        else:
            time_on_phone_by_number[from_number] = duration

        if to_number in time_on_phone_by_number:
            time_on_phone_by_number[to_number] += duration
        else:
            time_on_phone_by_number[to_number] = duration

    print(time_on_phone_by_number)

    # print(f"{} spent the longest time, {} seconds, on the phone during")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    longest_time_on_the_phone()


'''
SOLUTION:
- read calls
- create a data structure where each phone number can have a total
- attribute seconds to each number in the call
- sort this data structure
- print phone number whose total is highest

BIG QUESTION:

the average text message lenght is: 7 words*
it takes the average human 44 wpm seconds to write a text **
it takes the average human 250 seconds to read a text ***

* https://crushhapp.com/blog/k-wrap-it-up-mom
** https://www.ratatype.com/learn/average-typing-speed/
*** https://irisreading.com/what-is-the-average-reading-speed/

if ^ then: 
    with open('texts.csv', 'r') as f:
        reader = csv.reader(f)
        texts = list(reader)
'''
