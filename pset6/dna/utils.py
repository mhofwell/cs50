from sys import argv, exit
import csv
import re


def sanitize(argumentVector):
    if len(argumentVector) != 3:
        print("Missing command-line argument")
        exit(1)
