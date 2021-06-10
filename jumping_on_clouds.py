
def clouds(c):
    jumps = 0
    current = 0

    for _ in c:
        while current < (len(c) - 1):
            if c[current + 2] == 0:
                current = current + 2
                jumps = jumps + 1
            else:
                current = current + 1
                jumps = jumps + 1

    return jumps


c = [0, 0, 0, 1, 0, 0]

print(clouds(c))



