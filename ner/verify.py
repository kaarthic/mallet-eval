input1 = open('chn-verified.txt')
input2 = open('chn-result.txt')
token_count = 0
phrase_count = 0
found_count = 0
correct_count = 0

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
        token_count = token_count + 1
        print "line1: ",line1," line2: ",line2
        if cmp(line1, "O") != 0:
            phrase_count = phrase_count + 1
        if cmp(line2, "O") != 0:
            found_count = found_count + 1
        if cmp(line1, "O") != 0 and cmp(line2, "O") != 0 and cmp(line1, line2) == 0:
            correct_count = correct_count + 1

precision = float(correct_count) / float(found_count)
recall = float(correct_count) / float(phrase_count)
fb1 = precision * recall * 2 / (precision + recall)

print "processed " + str(token_count) + " tokens with " + str(phrase_count) + " phrases; found: " + str(found_count) + " phrases; correct: " + str(correct_count)
print "precision: " + str(precision * 100) + "%; recall: " + str(recall * 100) + "%; FB1: " + str(fb1 * 100)
