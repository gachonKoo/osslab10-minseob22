import sys

number = int(sys.argv[1])

for i in range(0, number):  # loop between 1 and number
    if number % i == 0:  # check if remainder is 0
        print(i, end=" ")

print()
