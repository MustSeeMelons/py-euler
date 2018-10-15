import sys
import time
import platform

if sys.platform == 'win32':
    default_timer = time.perf_counter
else:
    default_timer = time.time

start = 0

print("Using: " + platform.python_version())

def startProblem():
    start = default_timer()

def endProblem():
    end = default_timer()
    elapsed = (end - start) * 1000 * 1000
    print("Runtime: {:.2f}".format(elapsed) + " ns")



