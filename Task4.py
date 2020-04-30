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
outgoing_calls_set = set()
incoming_calls_set = set()
incoming_texts_set = set()
outgoing_texts_set = set()
texts_len = len(texts)
calls_len = len(calls)

for i in range(texts_len):
    outgoing_texts_set.add(texts[i][0])
    incoming_texts_set.add(texts[i][1])

for i in range(calls_len):
    outgoing_calls_set.add(calls[i][0])
    incoming_calls_set.add(calls[i][1])

print('These numbers could be telemarketers:')
outgoing_calls_set = sorted(outgoing_calls_set)
for outgoing_num in outgoing_calls_set:
    if (outgoing_num not in incoming_calls_set and 
        outgoing_num not in outgoing_texts_set and 
        outgoing_num not in incoming_texts_set
    ):
        print(outgoing_num)
    
#O(n log n)
#Again, the runtime will be linearithmic due to the sorted operation. 
#The linear complexity of the for-loops are insignificant in comparison when n grows large.
#The operations like variable assignment, adding to a set, checking if a set contains an element, etc have constant time complexity.
#https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt


    