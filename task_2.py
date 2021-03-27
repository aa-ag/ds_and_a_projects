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
def find_number_with_longest_time_on_the_phone():
    '''
     opens and reads calls.csv
     no need to open texts.csv since looking for duration
     creates a list of phone call lenghts, in total seconds
     prints out phone number of longest call in expected format
    '''

    f = open('calls.csv', 'r')
    reader = csv.reader(f)
    calls = list(reader)

    time_on_phone_by_number = dict()

    for row in calls:

        caller_number = row[0]
        call_recipient = row[1]

        duration = int(row[3])

        if caller_number in time_on_phone_by_number:
            time_on_phone_by_number[caller_number] += duration
        else:
            time_on_phone_by_number[caller_number] = duration

        if call_recipient in time_on_phone_by_number:
            time_on_phone_by_number[call_recipient] += duration
        else:
            time_on_phone_by_number[call_recipient] = duration

    phone_with_longest_duration = max(
        time_on_phone_by_number, key=lambda x: time_on_phone_by_number[x])

    print(
        f"{phone_with_longest_duration} spent the longest time,"
        f" {time_on_phone_by_number[phone_with_longest_duration]} seconds,"
        " on the phone during September 2016.")


###--- DRIVER CODE ---###
if __name__ == '__main__':
    find_number_with_longest_time_on_the_phone()
