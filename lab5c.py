#!/usr/bin/env python3
# Author ID: ekoleci

def add(number1, number2):
    try:
        return number1 + number2
    except TypeError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
