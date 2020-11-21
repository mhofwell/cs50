from sys import argv, exit
import csv
import re

# ensure proper input format from command line


def sanitize(argv):
    if len(argv) != 3:
        print("Missing command-line argument")
        exit(1)

# initialize the dnaDB dict using the dictionary file identified in input


def initDict(argv, dbFile, tmp):
    dbFile = open(argv[1], "r")
    if dbFile == None:
        exit(1)
    # initialize the dictionary file as a dictReader
    tmp = csv.DictReader(dbFile)
    return tmp

# read the DNA sequence to test into memory (buffer)


def initFile(tmp, argv):
    testFileName = open(argv[2], "r")
    if testFileName == None:
        exit(1)
    # read the testfile into a variable
    tmp = testFileName.read()
    testFileName.close()
    return tmp

# from the dnaDB, retrieve the names of all DNA strands we want to test the new sequence against


def getDnaNames(dnaNameList, dnaDB):
    i = 1
    # get all the fieldnames
    while i < len(dnaDB.fieldnames):
        dnaNameList.append(dnaDB.fieldnames[i])
        i += 1

# find the maximum number of sequences of the DNA strands that exist in the new sequence and add to a list


def getSequences(dnaNameList, results, testFile):
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

# search the dnaDB for a match between the list of sequences and entries in the dict.
# print the name of a match, if one exists


def findMatch(dnaDB, dnaNameList, results):
    fields = len(dnaDB.fieldnames) - 1
    # search the dnaDB for a match between results list and entries in the dict.
    for person in dnaDB:
        matchCount = 0
        for i in range(fields):
            if int(person[dnaNameList[i]]) == int(results[i]):
                matchCount += 1
            if matchCount == fields:
                print(person['name'])
                exit(0)

    print("No match.")

# close the DictReader


def closeFile(dbFile):
    dbFile.close()
