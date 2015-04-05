#!/usr/bin/env python

import sys

for line in sys.stdin:
    for word in line.split():
        # Remove special characters and words longer than 3
        word = word.replace('"', '')
        word = word.replace('.', '')
        word = word.replace(':', '')
        word = word.replace('*', '')
        word = word.replace(',', '')
        word = word.replace('(', '')
        word = word.replace(')', '')
        word = word.replace('?', '')
        word = word.replace('!', '')
        word = word.replace('-', '')
        word = word.replace('0', '')
        word = word.replace('1', '')
        word = word.replace('2', '')
        word = word.replace('3', '')
        word = word.replace('4', '')
        word = word.replace('5', '')
        word = word.replace('6', '')
        word = word.replace('7', '')
        word = word.replace('8', '')
        word = word.replace('9', '')
        word = word.replace(';', '')
        word = word.replace('\'', '')
        word = word.lower()
        if len(word) > 3: word = ''
        if word == '': word = 'OTHER'
        print '%s\t%s' % (word, 1)
