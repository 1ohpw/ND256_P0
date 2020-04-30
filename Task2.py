"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
calls_len = len(calls)
duration_dict = {}

for i in range(calls_len):
    if calls[i][2][3:10] == '09-2016':
        if duration_dict.get(calls[i][0]):
            duration_dict[calls[i][0]] += int(calls[i][3])
        else:
            duration_dict[calls[i][0]] = int(calls[i][3])
        
        if  duration_dict.get(calls[i][1]):
            duration_dict[calls[i][1]] += int(calls[i][3])
        else:
            duration_dict[calls[i][1]] = int(calls[i][3])

max_duration = 0
max_duration_phone_num = 0
for phone_num in duration_dict:
    if duration_dict[phone_num] > max_duration:
        max_duration = duration_dict[phone_num]
        max_duration_phone_num = phone_num

print(max_duration_phone_num + ' spent the longest time, ' + str(max_duration) + ' seconds, on the phone during September 2016.')

#O(n)
#I iterate through the input successively, so the runtime will be linear. 
#Incrementing integers, accessing elements in lists/dictionaries, etc have constant time complexity, so these operations can be disregarded.
#The slice operation used to compare the date will always check the same string length, so it will not scale as n grows.
#https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt