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
total = set()
total_numbers = set()
list1,list2 = [],[]
for i in calls:
    total.add(i[0])
    total_numbers.add(i[1])
for i in total:
        if i not in total_numbers:
            list1.append(i)
total.clear()
total_numbers.clear()
for i in texts:
    total.add(i[0])
    total_numbers.add(i[1])
for i in list1:
    if i not in total_numbers or i not in total:
        list2.append(i)
print("These numbers could be telemarketers: ")
for i in sorted(list2):
    print(i)
print("The list of numbers should be print out one per line in lexicographic order with no duplicates.")
