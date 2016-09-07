def insertSort(buf):
    for i in range(1, len(buf)):
        while i > 0 and buf[i] < buf[i - 1]:
            buf[i], buf[i - 1] = buf[i - 1], buf[i]
            i -= 1
    return buf


def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False