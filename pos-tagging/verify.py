input1 = open('eng-verified.txt')
input2 = open('eng-result.txt')
word_count = 0
error_count = 0
miss_count = 0

while 1:
    line1 = input1.readline()
    line2 = input2.readline()
    if not line1 or not line2:
        break
    line1 = line1.strip('\n')
    line2 = line2.strip('\n')
    line1 = line1.strip(' ')
    line2 = line2.strip(' ')
    if len(line1) > 0 or len(line2) > 0:
        print "line1: ",line1," line2: ",line2
        word_count = word_count + 1
        if cmp(line2, "") == 0:
            miss_count = miss_count + 1
            continue
        if cmp(line1, line2) != 0:
            error_count = error_count + 1

print "Word Count: ",word_count,"\nError Count: ",error_count,"\nMiss Count: ",miss_count
