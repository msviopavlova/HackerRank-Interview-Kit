
def clouds(c):
    jumps = 0
    current = 0

    for _ in c:
        if (current + 1) < len(c)-2:
            if c[current + 2] == 0:
                current = current + 2
                jumps = jumps + 1
            else:
                current = current + 1
                jumps = jumps + 1
        elif current == len(c) - 1:
            if c[current] == 0:
                jumps = jumps +1
                current = current + 1

    return jumps


c = [0, 0, 0, 1, 0, 0]

print(clouds(c))



