#!/usr/bin/python
# convert mallet output to conlleval compatible format
# NOTE: conlleval format contains 4 columns, including text, pos, correct chunking,
# and mallet chunking

input1 = open('chn-verified.txt')
input2 = open('chn-result.txt')

while 1:
    line1 = input1.readline()
    line2 = input2.readline()
    if not line1 or not line2:
        break
    line1 = line1.strip('\n')
    line2 = line2.strip('\n')
    line1 = line1.strip('\r')
    line2 = line2.strip('\r')
    line2 = line2.strip(' ')
    if not line1:
        print ""
    else:
        line1 = line1.split(' ')
        print line1[0].strip(' '),line1[1].strip(' '),line1[2].strip(' '),line2
