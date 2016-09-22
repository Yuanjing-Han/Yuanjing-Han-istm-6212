#!/usr/bin/env python

"""
A filter that remove 20 stop words that I generated from women.txt.
"""

import fileinput
stopwords = ['and','the','to','of','her','it','in','you','she','for','was','as','that','with','he','but','jo','so','his','at']

def process(line):
    """For each line of input, check whether it is in the stopwords list; if no, print it out."""
    word = line[:-1]
    if word not in stopwords:
        print(word)

for line in fileinput.input():
    process(line)
