def fibonacci_sequence(x):
    a = 0
    b = 1
    list = []
    for i in range(0,x):
        if i % 2 == 1:
            a = a + b
            list.append(a)
        else:
            b = a + b
            list.append(b)
    print(list)

print(fibonacci_sequence(10))