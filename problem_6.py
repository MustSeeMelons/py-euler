# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#  (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
from util.utils import startProblem, endProblem
import math

startProblem()

sum = 0
square = 0
for i in range(1, 101):
    sum += i
    square += math.pow(i, 2)

result = math.fabs(square - math.pow(sum, 2))

print("The difference is: " + str(result))
endProblem()