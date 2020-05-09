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
total = set()
for i in calls:
    total.add(i[0])
    total.add(i[1])
dic = {}
d = 0
for i in total:
    for j in calls:
        if i==j[0] or i==j[1]:
            d = int(j[3]) + d
        dic.update( {i : d} ) 
    d = 0

l = []
for i in dic:
    l.append(dic[i])
vallll = max(l)

def get_key(val): 
    for key, value in dic.items(): 
         if val == value: 
             return key
keey = get_key(max(l))
print(keey + " spend the longest time, "+ str(vallll) + " seconds, on the phone during September 2016.")
