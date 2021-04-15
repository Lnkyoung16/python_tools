def cipher_check(x):
    length = len(str(x))
    cipher = []
    result = []
    for z in range(0, length):
        cipher.append(10**(length - z - 1))
        temp = 0
    for c in cipher:
        temp = x / c
        temp = int(temp)
        result.append(temp)
        x = x - (temp * c)
    return result