import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# def countingValleys(steps, path):
#     level = 0
#     valleys = 0
#     for p in path:
#         if p == "U":
#             level = level + 1
#             if level > 0:
#                 print(f"mountain step {level}")
#             elif level == 0:
#                 print("SEA after VALLEY")
#                 valley = valley + 1
#         elif p == "D":
#             level = level - 1
#             if level < 0:
#                 print(f"we are in VALLEY {level}")
#             elif level == 0:
#                 print("SEA after MOUNTAIN")
#
#
# countingValleys(, ["U","U","U","D","D","D","U","U"])
#





def countingValleys(steps, path):
    level = 0
    valleys = 0
    for steps, p in enumerate(path):
        if p == "U":
            level = level + 1
            if level > 0:
                print(f"mountain step {level}")
            elif level == 0:
                print("SEA after VALLEY")
                valleys = valleys + 1
                print(f"{valleys} valleys")
        elif p == "D":
            level = level - 1
            if level < 0:
                print(f"we are in VALLEY {level}")
            elif level == 0:
                print("SEA after MOUNTAIN")
    print(f"{valleys} valleys")

countingValleys(16, "DDUUUUDDDDUUUUDD")



