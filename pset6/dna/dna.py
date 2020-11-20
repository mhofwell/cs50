import cs50
import re
import math
import csv
from utils import sanitize
from sys import argv, exit


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

    # compute longest run of consecutive repeats of the STR in the DNA sequence
    if re.search(dnaDB.fieldnames[1], memTestFile):
        print("Found")
        sampleAG = 0
        sampleAA = 0
        sampleTA = 0

    # look for a match between the test data and the dnaDB
    for row in dnaDB:
        AG = int(row["AGATC"])
        AA = int(row["AATG"])
        TA = int(row["TATC"])

        if sampleAG == AG and sampleAA == AA and sampleTA == TA:
            print(row["name"])
            exit(0)
        else:
            break

    print("No match found.")


main()
