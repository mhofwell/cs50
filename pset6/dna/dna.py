import re
import math
import csv
from utils import sanitize
from sys import argv, exit

countStrand1 = 0
countStrand2 = 0
countStrand3 = 0
countStrand4 = 0
countStrand5 = 0
countStrand6 = 0
countStrand7 = 0
countStrand8 = 0


def main():

    # sanitize command line input
    sanitize(argv)

    # open CSV and read contents into memory
    # get the filename or the database
    dnaData = argv[1]

    # get the file to test against the DB
    testFile = argv[2]

    # open DNA sequence and read its contents into memory
    database = open(dnaData, "r")
    dnaDB = csv.DictReader(database)

    # load testfile data into dict in memory
    with open(testFile, "r") as testFile:
        memTestFile = testFile.read()

    matchCount = 0

    dnaStrand1 = dnaDB.fieldnames[1]
    dnaStrand2 = dnaDB.fieldnames[2]
    dnaStrand3 = dnaDB.fieldnames[3]
    dnaStrand4 = dnaDB.fieldnames[4]
    dnaStrand5 = dnaDB.fieldnames[5]
    dnaStrand6 = dnaDB.fieldnames[6]
    dnaStrand7 = dnaDB.fieldnames[7]
    dnaStrand8 = dnaDB.fieldnames[8]

    countStrand1 = re.findall(r'(?:'+dnaStrand1+')+', memTestFile)
    if countStrand1:
        maxSequence = max(countStrand1, key=len)
        countStrand1 = (len(maxSequence)//len(dnaStrand1))

    countStrand2 = re.findall(r'(?:'+dnaStrand2+')+', memTestFile)
    if countStrand2:
        maxSequence = max(countStrand2, key=len)
        countStrand2 = (len(maxSequence)//len(dnaStrand2))

    countStrand3 = re.findall(r'(?:'+dnaStrand3+')+', memTestFile)
    if countStrand3:
        maxSequence = max(countStrand3, key=len)
        countStrand3 = (len(maxSequence)//len(dnaStrand3))

    countStrand4 = re.findall(r'(?:'+dnaStrand4+')+', memTestFile)
    if countStrand4:
        maxSequence = max(countStrand4, key=len)
        countStrand4 = (len(maxSequence)//len(dnaStrand4))

    countStrand5 = re.findall(r'(?:'+dnaStrand5+')+', memTestFile)
    if countStrand5:
        maxSequence = max(countStrand5, key=len)
        countStrand5 = (len(maxSequence)//len(dnaStrand5))

    countStrand6 = re.findall(r'(?:'+dnaStrand6+')+', memTestFile)
    if countStrand6:
        maxSequence = max(countStrand6, key=len)
        countStrand6 = (len(maxSequence)//len(dnaStrand6))

    countStrand7 = re.findall(r'(?:'+dnaStrand7+')+', memTestFile)
    if countStrand7:
        maxSequence = max(countStrand7, key=len)
        countStrand7 = (len(maxSequence)//len(dnaStrand7))

    countStrand8 = re.findall(r'(?:'+dnaStrand8+')+', memTestFile)
    if countStrand8:
        maxSequence = max(countStrand8, key=len)
        countStrand8 = (len(maxSequence)//len(dnaStrand8))

    for row in dnaDB:
        if countStrand1 == int(row[dnaStrand1]) and countStrand2 == int(row[dnaStrand2]) and countStrand3 == int(row[dnaStrand3]) and countStrand4 == int(row[dnaStrand4]) and countStrand5 == int(row[dnaStrand5]) and countStrand6 == int(row[dnaStrand6]) and countStrand7 == int(row[dnaStrand7]) and countStrand8 == int(row[dnaStrand8]):
            print(row['name'])
            exit(1)

    print("No match.")


main()
