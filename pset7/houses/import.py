from sys import argv
import re
import math
import csv
import sqlite3

studentList = {}

# check command line arguments
if len(argv) != 2:
    print("Proper usage: python <script name> <csv name>")
    exit(1)

db = sqlite3.connect("students.db")
cursor = db.cursor()

# open CSV file given by command line args
file = open(argv[1], "r")
if file == None:
    exit(2)
studentList = csv.DictReader(file)

for row in studentList:
    print(row)
    # for each row, parse name
    name = row['name']
    nameList = name.split()
    if len(nameList) == 3:
        fn = nameList[0]
        mn = nameList[1]
        ln = nameList[2]
    else:
        fn = nameList[0]
        mn = None
        ln = nameList[1]

    # insert each student into students table of students.db
    vars = (fn, mn, ln, row['house'], row['birth'])
    query = "INSERT INTO students(first, middle, last, house, birth) VALUES(?,?,?,?,?)"

    cursor.execute(query, vars)

    db.commit()
    