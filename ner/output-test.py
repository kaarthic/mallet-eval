#!/usr/bin/python
# output test file for mallet

input = open('chn-verified.txt')
for line in input:
    if len(line.split(' ')) > 1:
        print line.split(' ')[0].split("\n")[0]
    else:
        print ''
