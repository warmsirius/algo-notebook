def KMP(str1, str2):
    m = len(str2)
    n = len(str1)
    if str1 == "" or str2 == "" or len(str1) < 1 or len(str2) < 1:
        return
    i1 = 0
    i2 = 0
    nextArray = getNextArray(str2)
    while (i1 < n) and (i2 < m):
        if str2[i2] == str1[i1]:
            i2 += 1
            i1 += 1
        elif nextArray[i2] == -1:
            i1 += 1
        else:
            i2 = nextArray[i2]
    if i2 == m:
        return i1 - i2
    else:
        return -1


def getNextArray(str2):
    m = len(str2)
    nextArray = [0] * m
    nextArray[0] = -1

    if m == 1:
        return nextArray
    nextArray[1] = 0
    pos = 2
    index = 0
    while pos < m:
        if str2[pos - 1] == str2[index]:
            index += 1
            nextArray[pos] = index
            pos += 1
        elif index > 0:
            index = nextArray[index]
        else:
            pos += 1
    return nextArray


print(KMP("abcabcdabcde", "abcde"))