"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
texts_len = len(texts) 
calls_len = len(calls) 
unique_phone_nums = set()
for i in range(texts_len):
    unique_phone_nums.add(texts[i][0])
    unique_phone_nums.add(texts[i][1])
for i in range(calls_len):
    unique_phone_nums.add(calls[i][0])
    unique_phone_nums.add(calls[i][1])
print('There are ' + str(len(unique_phone_nums)) + ' different telephone numbers in the records.')

#O(n)
#This will have O(n) runtime since I iterate through the entire dataset (both lists successively). 
#Runtime will grow linearly as the size of the input grows.
#Within each loop, only constant operations are done (adding to a set, and accessing elements in lists).
#Getting the length of the set also has constant time complexity.
#https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
