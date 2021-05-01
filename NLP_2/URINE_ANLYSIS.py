import re
import csv

pattern = r"(?P<Exam>^[A-Za-z\s]+?)+:\s+(?P<result>[0-9a-zA-Z-\s.()+\/]+)$"

fields=["Exman" ,"Result"]

file=open('URINE_ANLYSIS.txt','r')

matchesRow = []

lines=file.readlines()

for line in lines:
    match=re.match(pattern,line)
    if match:
        matchesRow.append(match.groups())
        print(match.groups())
    else:
        print("no match")

with open('URINE_ANLYSIS.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(matchesRow)