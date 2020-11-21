import re
import math
import csv
from utils import sanitize, getDnaNames, getSequences, findMatch, closeFile, initDict, initFile
from sys import argv, exit

# initialize an array for DNA fieldnames
dnaNameList = []
# initialize a results array to hold the count of the longest DNA match sequences
results = []
# initialize a pointer for the database input to NULL
dbFile = None
# initialize an empty dict to hold the DNA dict created from the database input
dnaDB = {}
# initialize a temp variable for utilities
tmp = None
# initialize a buffer to hold the contents of the DNA sequence to process
testFile = None


def main():

    # ensure proper input format
    sanitize(argv)

    # get dict filename and initialize it
    dnaDB = initDict(argv, dbFile, tmp)

    # prepare the testfile and read it to memory
    testFile = initFile(tmp, argv)

    # get names of the DNA to test
    getDnaNames(dnaNameList, dnaDB)

    # iterate through the sample DNA with each fieldname
    getSequences(dnaNameList, results, testFile)

    # search the dnaDB for a match between results list and entries in the dict.
    findMatch(dnaDB, dnaNameList, results)

    # close the DictReader
    closeFile(dbFile)


main()
