#!/usr/bin/env python

"""
A filter that convert input into lower case.
"""

import fileinput


def process(line):
    """For each line of input, lowercase it."""
    print(line[:-1].lower())


for line in fileinput.input():
    process(line)
