f = open('sample.txt', 'r')
lines = f.readlines()
f.close()

sum = 0

for line in lines:
    sum += int(line)

average = sum/len(lines)

f = open('sample.txt', 'w')
f.write(str(average))
f.close()