import math
def repeatedString(s, n):
    # Write your code here
    repetition = math.ceil(n/len(s))
    r = s*repetition
    s_new = r[:n]
    print(f"{s_new} new string")
    result = []
    for char in s_new:
        if char == "a":
            result.append(char)
   # print(result)
    LONG_INTEGER = len(result)
    return LONG_INTEGER



print(repeatedString("a", 100))