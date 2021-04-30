import re
import csv

# header of csv file
fields=["Component" ,"Your Value", "Standard Range" ,"Units(if exists)"] #csv file labels
#creating regex patterns
# pattern1=r"(?P<measure>[a-zA-Z]+[a-zA-Z()\s-]*:?)(?P<value>(?:\s*-?\d+.?\d*\s*-?\d*)|(?:\s*[a-zA-Z]+.*))(?P<unit>\s*.*)" 
pattern =r"(?P<Component>[a-zA-Z\s()-]+)\s*:\s*(?P<Value>[0-9\.]{1,6})\s*(?P<Range>[0-9\.]{1,5}\s*-\s*[0-9\.]{1,5})\s*(?P<Unit>[a-zA-Z//%013^\s]+)"
# writing to csv file 
with open('part4.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields)
    #read the text data line by line
    file=open('part4.txt','r')
    lines=file.readlines()
    for line in lines:
        #match the two patterns
        match=re.match(pattern,line)
        if match:
            print("pattern1:"+ "Component"+"=="+match.group("Component")+
                    " value"+"=="+match.group("Value")
                    +" range"+"=="+match.group("Range")
                    + " Unit"+"=="+match.group("Unit"))
            #remove /n symbole from the end of the line if found
            row=match.groups()
            row=list(row)
            for i in range(4):
                row[i]=row[i].split('\n')[0]
            print("pat:",row)
            csvwriter.writerow(match.groups()) #write to csv file  
        else:
            print("no match")
# clear csv file from empty lines
import pandas as pd
df = pd.read_csv('part4.csv')
df.to_csv('part4.csv', index=False)