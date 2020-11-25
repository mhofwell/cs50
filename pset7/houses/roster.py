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
print(argv[0])
# query database for all students in house
db = sqlite3.connect("students.db")
cursor = db.cursor()
house = argv[1]
query = "SELECT * FROM students WHERE "
cursor.execute("select * from students;")

rows = cursor.fetchall()

for row in rows:
    print(str(row[0]))
