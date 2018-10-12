# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import platform
import math
import sys
import time

if sys.platform == 'win32':
    default_timer = time.perf_counter
else:
    default_timer = time.time

start = default_timer()

print("Using: " + platform.python_version())


def isPalindrome(number):
    sNum = str(number)
    sLen = - 1
    hStr = sNum[0:math.floor(len(sNum) / 2)]

    for idx, c in enumerate(hStr):
        if(c != sNum[sLen - idx]):
            return False

    return True


def sequencer():
    def next():
        for i in range(100, 1000):
            yield i

    return next


largest = 0

first_seq = sequencer()
second_seq = sequencer()

for i in first_seq():
    for j in second_seq():
        num = i * j
        if(isPalindrome(num) and num > largest):
            largest = num

end = default_timer()
elapsed = (end - start) * 1000 * 1000
print("Runtime: {:.2f}".format(elapsed) + " ns")
print("Largest 3 digit number product palindrome: " + str(largest))
