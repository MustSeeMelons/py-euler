# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math
from util.utils import startProblem, endProblem

def isPrime(num):
    if(num == 1 or num <= 0):
        return False
    for i in range(2, math.floor(num / 2) + 1):
        if(num % i == 0):
            return False

    return True

def primeSequencer():
    counter = 1

    def nextPrime():
        nonlocal counter  # Cant mutate closure variables otherwise
        counter += 1
        while not isPrime(counter):
            counter += 1
        return counter

    return nextPrime

startProblem()

seq = primeSequencer()

prime = seq()
counter = 1
while counter < 10001:
    prime = seq()
    counter +=1 

print("The 10,001 st: " + str(prime))
endProblem()