import math
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(count, ar):
    for num in ar:
        if len(set(ar)) == len(ar):
            return 0
        elif len(set(ar)) < len(ar):
            difference = len(ar)-len(set(ar))
            




result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
print(result)