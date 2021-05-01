import re
import csv
import pandas as pd

pattern = r"(?P<component>^[\%?\#?\w]+)+\s*(?P<Value>[\d\.]+)+\s*(?P<Minimum>[\d\.]+)+\-(?P<Maximum>[\d\.]+)+\s*(?P<Units>[\w\%\/\^]+)"

file=open('blood.txt','r')
dta_lines=file.readlines()
component_data = []
for line in dta_lines:
    match=re.match(pattern,line)
    if match:
        component_data.append(match.groups())
    else:
        continue
        #No action is taken

df = pd.DataFrame(data=component_data)
df.columns = ["Component" ,"Current Value", "Minimum Range", "Maximum Range" ,"Units"]
df.to_csv("blood.csv", index=False)