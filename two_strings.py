def twoStrings(s1, s2):
    # Write your code here
    common = None

    for l in s1:
        if l in s2:
            common = l

    if common != None:
        return "YES"
    else:
        return "NO"