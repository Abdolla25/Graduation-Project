import re
import csv

pattern = r"(?P<component>^[A-Z-\s]+)+(?P<Value>[0-9.]+)+\s*(?P<StandardRange>[0-9-.\s]+)+(?P<Unit>[A-Z%\/]+)"

fields=["Component" ,"Your Value", "Standard Range" ,"Units"]

file=open('CBC.txt','r')

matchesRow = []

lines=file.readlines()

for line in lines:
    match=re.match(pattern,line)
    if match:
        matchesRow.append(match.groups())
        print(match.groups())
    else:
        print("no match")

with open('CBC.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(matchesRow)