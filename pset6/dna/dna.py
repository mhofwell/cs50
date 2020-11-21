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

    # ensure proper input format from command line
    sanitize(argv)

    # initialize the dnaDB dict using the dictionary file identified in input
    dnaDB = initDict(argv, dbFile, tmp)

    # read the DNA sequence to test into memory (buffer)
    testFile = initFile(tmp, argv)

    # from the dnaDB, retrieve the names of all DNA strands we want to test the new sequence against
    getDnaNames(dnaNameList, dnaDB)

    # find the maximum number of sequences of the DNA strands that exist in the new sequence and add to a list
    getSequences(dnaNameList, results, testFile)

    # search the dnaDB for a match between the list of sequences and entries in the dict.
    # print the name of a match, if one exists
    findMatch(dnaDB, dnaNameList, results)

    # close the DictReader
    closeFile(dbFile)


main()
