# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from util.utils import startProblem, endProblem

numRange = (2, 21)

startProblem()

num = 1
found = False

while not found:
    found = True
    for i in range(numRange[0], numRange[1]):
        if(num % i != 0):
            num += 1
            found = False
            break


print("Magic number: " + str(num))
endProblem()
