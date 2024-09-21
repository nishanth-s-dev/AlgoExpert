def runLengthEncoding(s):
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] and count < 9:
            count += 1
        else:
            res.append(str(count) + s[i - 1])
            count = 1

    res.append(str(count) + s[-1])
    print(res)
    return "".join(res)