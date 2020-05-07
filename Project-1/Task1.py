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

Count = set()

for val in texts:
    Count.add(val[0])
    Count.add(val[1])
for val in calls:
    Count.add(val[0])
    Count.add(val[1])

a=str(len(Count))

print("There are "+a + " different telephone numbers in the records")
