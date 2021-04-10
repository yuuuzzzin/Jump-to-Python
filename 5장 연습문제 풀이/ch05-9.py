import sys

nums = sys.argv[1:]

sum = 0
for num in nums:
    sum += int(num)

print(sum)