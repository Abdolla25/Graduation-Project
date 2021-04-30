import re
import csv

# header of csv file
fields=["Test" ,"Value"] #csv file labels
#creating regex patterns
pattern =r"(?P<Test>.*):(?P<Value>.*)"
# writing to csv file 
with open('part5.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields)
    #read the text data line by line
    file=open('part5.txt','r')
    lines=file.readlines()
    for line in lines:
        #match the two patterns
        match=re.match(pattern,line)
        if match:
            print("pattern1:"+ "Component"+"=="+match.group("Test")+
                    " value"+"=="+match.group("Value"))
            print("pat:",match.groups())
            csvwriter.writerow(match.groups()) #write to csv file  
        else:
            print("no match")
#clear csv file from empty lines
import pandas as pd
df = pd.read_csv('part5.csv')
df.to_csv('part5.csv', index=False)