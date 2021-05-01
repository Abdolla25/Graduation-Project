import re
import csv

pattern1 = r"(?P<component>^[A-Za-z-\s()]+)+:?\s+(?P<Value>[0-9.]+)+\s*(?P<StandardRange>[0-9-.\s\/x^]+[a-zA-Z^\/0-9%]+\n)"

pattern2 = r"(?P<component>^[A-Za-z-\s()]+)+:?\s+(?P<RelativeCount>[0-9]+\s*[0-9]+\s?-\s?[0-9]+)+\s*(?P<AbsoluteCount>[0-9.\s-]+)"


fields1=["BlooHed Picture" ,"Reference", "Range"]

fields2=["Test" ,"Relative count %", "Absolute count K/ul"]

file=open('HEMATOLOGY_REPORT.txt','r')

matchesRow1 = []
matchesRow2 = []



lines=file.readlines()

counter = 0

for line in lines: 
    if(counter<12):
        match=re.match(pattern1,line)
    else:
        match=re.match(pattern2,line)
    if match:
        print("ok")
       
        if(counter<12):
            matchesRow1.append(match.groups())
        else:
            matchesRow2.append(match.groups())
        print(match.groups())
        counter= counter + 1
        print(counter)
    else:
        print("no match")

with open('HEMATOLOGY_REPORT.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields1)
    writer.writerows(matchesRow1)
    writer.writerow(fields2)
    writer.writerows(matchesRow2)