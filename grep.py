#!/usr/bin/env python

"""
A filter that split lines of text into one word per line.
"""

import fileinput
import re

def process(line):
    """For each line of input, split it into one word per line."""   
    line_no_punc = re.compile('\w+')
    line = line_no_punc.findall(line)
    for word in line:
        if len(word)>=2:
            print(word)
    
for line in fileinput.input():
    process(line)
