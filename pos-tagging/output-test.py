input = open('eng-verified.txt')
for line in input:
    if len(line.split(' ')) > 1:
        print line.split(' ')[1].split("\n")[0]
    else:
        print ''
