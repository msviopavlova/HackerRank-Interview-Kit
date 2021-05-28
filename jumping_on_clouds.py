
def clouds(c):
    jumps = 0

    for count, value in enumerate(c):
        if len(c) - 1 != count:
            if count == 0:
                continue
            elif value == 0:
                if c[count-1]==1:
                    jumps = jumps +1
                if c[count + 2] == 0 and c[count+1] == 0:
                    continue
                elif c[count +1] == 1:
                    jumps = jumps + 1
                elif c[count+1] == 0 and c[count+2] == 1:
                    continue
                elif c[count+1] == 0:
                    jumps = jumps + 1
        else:
            if value == 0:
                jumps = jumps + 1


    return jumps



c = [0, 0, 1, 0, 0, 1, 0]

print(clouds(c))



