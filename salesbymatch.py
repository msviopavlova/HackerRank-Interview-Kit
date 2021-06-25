def sockMerchant(n, ar):
    pairs = 0
    unfinished = []
    for char in ar:
        if char in unfinished:
            pairs += 1
            unfinished.remove(char)

        elif char not in unfinished:
            unfinished.append(char)

    return pairs











lol = [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(9, lol))

