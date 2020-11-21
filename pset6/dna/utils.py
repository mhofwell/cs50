from sys import argv, exit
import csv
import re


def sanitize(argv):
    if len(argv) != 3:
        print("Missing command-line argument")
        exit(1)


def initDict(argv, dbFile, tmp):
    dbFile = open(argv[1], "r")
    if dbFile == None:
        exit(1)
    # initialize the dictionary file as a dictReader
    tmp = csv.DictReader(dbFile)
    return tmp

# open and read the contents of the testfile to memory


def initFile(tmp, argv):
    testFileName = open(argv[2], "r")
    if testFileName == None:
        exit(1)
    # read the testfile into a variable
    tmp = testFileName.read()
    testFileName.close()
    return tmp


def getDnaNames(dnaNameList, dnaDB):
    i = 1
    # get all the fieldnames
    while i < len(dnaDB.fieldnames):
        dnaNameList.append(dnaDB.fieldnames[i])
        i += 1

# iterate through the sample DNA with each fieldname


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


def closeFile(dbFile):
    dbFile.close()
