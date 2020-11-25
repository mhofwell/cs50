from sys import argv
import re
import math
import csv
import sqlite3

# TODO
# python roster.py Gryffindor

# check command line arguments
if len(argv) != 2:
    print("Proper usage: python <script name> <csv name>")
    exit(1)

# query database for all students in house
db = sqlite3.connect("students.db")
cursor = db.cursor()

house = argv[1]
result = cursor.execute("SELECT * FROM students WHERE house=?", (house,))

rows = cursor.fetchall()

for row in rows:
    firstName = row[1]
    middleName = row[2]
    lastName = row[3]
    house = row[4]
    birth = row[5]
    if middleName == None:
        print(f"{firstName} {lastName} {house} born, {birth}")
    else:
        print(f"{firstName} {middleName} {lastName} {house} born, {birth}")
