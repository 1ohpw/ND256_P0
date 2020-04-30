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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
total_bang_outgoing = 0
count_bang_to_bang = 0
codes_prefixes = set()
for call in calls:
  if call[0][:5] == '(080)':
    total_bang_outgoing += 1
    if call[1][0] == '(':
      if call[1][:5] == '(080)':
        count_bang_to_bang += 1 
      end_parenthesis = call[1].index(')')
      codes_prefixes.add(call[1][:end_parenthesis + 1])
    elif call[1][0] == '7' or call[1][0] == '8' or call[1][0] == '9':
      codes_prefixes.add(call[1][:4])
    else:
      codes_prefixes.add('140')

codes_prefixes = sorted(codes_prefixes)
print('The numbers called by people in Bangalore have codes:')
for code_prefix in codes_prefixes:
  print(code_prefix)

percentage = round(count_bang_to_bang / total_bang_outgoing * 100, 2)
print(str(percentage) + ' percent of calls from fixed lines in Bangalore are calls' + 
      ' to other fixed lines in Bangalore')

#O(n log n)
#Here I am not completely sure. My best guess is O(n log n) since that is the runtime of the sorted method. 
#The successive loops will have linear runtime. This can be disregarded since the O(n log n) is significantly greater for large n.
#Though string slice operations are used within the first loop, this can be disregarded too -
#since each slice operation will still take the same time as n grows.
    


