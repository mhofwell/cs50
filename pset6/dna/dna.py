import re
import math
import csv
from utils import sanitize
from sys import argv, exit

argVector = argv

# ensure proper input format
sanitize(argVector)

# open the dictionary file
dbFile = open(argv[1], "r")
if dbFile == None:
    exit(1)

# initialize the dictionary file as a dictReader
dnaDB = csv.DictReader(dbFile)

# open the testfile
testFileName = open(argv[2], "r")
if testFileName == None:
    exit(1)

# read the testfile into a variable
testFile = testFileName.read()
testFileName.close()

# initialize an array of fieldnames
dnaNameList = []
i = 1

# get all the fieldnames
while i < len(dnaDB.fieldnames):
    dnaNameList.append(dnaDB.fieldnames[i])
    i += 1

# initialize a results array to hold the count of each
# DNA fieldname
results = []

# iterate through the sample DNA with each fieldname
for dna in dnaNameList:
    count = re.findall(r'(?:'+dna+')+', testFile)
    if count:
        maxSequence = max(count, key=len)
        patternLength = int(len(maxSequence) / len(dna))
        # put the result into a separate array
        if patternLength > 0:
            results.append(patternLength)
    # if a sequence doesn't exist, exit and declare no match.
    else:
        print('No match.')
        exit(2)

fields = len(dnaDB.fieldnames) - 1

# search the dnaDB for a match between results list and entries in the dict.
for person in dnaDB:
    matchCount = 0
    for i in range(fields):
        if int(person[dnaNameList[i]]) == int(results[i]):
            matchCount += 1
        if matchCount == fields:
            print(person['name'])
            dbFile.close()
            exit(0)

print("No match.")
dbFile.close()
