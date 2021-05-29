
def clouds(c):
    jumps = 0

    for count, value in enumerate(c):
        if (count == 0 or count == c[-1]) and value == 0:
            if c[count+1] == 0 and c[count+2] == 0:
                count = count + 2
                jumps = jumps + 1
            if c[count+1] == 0 and c[count+2] == 1:
                jumps = jumps + 1


    return jumps



c = [0, 0, 1, 0, 0, 1, 0]

print(clouds(c))



