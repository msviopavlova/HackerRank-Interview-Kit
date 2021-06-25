# import math
# def repeatedString(s, n):
#     # Write your code here
#     repetition = math.ceil(n/len(s))
#     print(f"{repetition} times fits in {n}")
#     r = s*repetition
#     print(f"{r} this is r var")
#     # s_new = r[:n]
#     # print(f"{s_new} new string")
#     result = []
#     for char in r:
#         if char == "a":
#             result.append(char)
#    # print(result)
#     LONG_INTEGER = len(result)
#     return LONG_INTEGER


def repeatedString(s, n):

    letters = []
    for char in s:
        if char == "a":
            letters.append(char)
    leftover = n % len(s)

    times = n // len(s)
    amountofains = len(letters)
    extras = []
    for d in s[:leftover]:
        if d == "a":
            extras.append(d)

    result = (amountofains * times) + len(extras)
    return result






print(repeatedString("aba", 10))