#Code to take a edge file, create a dictionary where the column B is used as a key and column A are used as values.  The dictionary is exported as a CSV with each line holding a different key:value set.

import csv

#Have the user input a file
filename = input('Enter file name: ')

#Set up an empty dictionary
mydict = {}

#Open the file
with open(filename) as r:
    reader = csv.reader(r)  
    # skip header row
    next(reader, None)
    # process data rows
    for rows in reader:   
        k = rows[1] #sets key value according to fields in Column B
        v = rows[0] #sets values according to fields in Column A
       
        # Get key ifrom dict if needed, prepopulate value with empty list
        key = mydict.setdefault(k,[])

        # append data to list
        key.append(v)

#Printing the dictionaries in a csv so each key has a different line
with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])

print("File has been created")
