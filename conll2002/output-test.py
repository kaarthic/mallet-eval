#!/usr/bin/python
# output test file for mallet

input = open('esp.testa')
for line in input:
    if len(line.split(' ')) > 1:
        print line.split(' ')[0],line.split(' ')[1]
    else:
        print ''
