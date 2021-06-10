

def clouds(c):
    jumps = 0
    current = 0

    while current < len(c)-1:
        if current+2 <= len(c)-1 and c[current + 2] == 0:
            current = current + 2
            jumps = jumps + 1
        else:
            current = current + 1
            jumps = jumps + 1

    return jumps




c = [0, 0, 1, 0, 0, 1, 0]


print(clouds(c))



