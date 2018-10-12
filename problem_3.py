# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

import time
import platform
import math
import sys

if sys.platform == 'win32':
    default_timer = time.perf_counter
else:
    default_timer = time.time

start = default_timer()

print("Using: " + platform.python_version())

# number = int(input("Enter number for which to get prime factors: "))
number = 600851475143


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


curNum = number
seq = primeSequencer()

while True:
    prime = seq()
    if(curNum % prime == 0):
        curNum = curNum / prime

        if(isPrime(curNum)):
            end = default_timer()
            elapsed = (end - start) * 1000 * 1000
            print("Runtime: {:.2f}".format(elapsed) + " ns")
            print("Largest factor is: " + str(curNum))
            break
