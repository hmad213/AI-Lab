def details(*args):
    sum = 0
    for x in args:
        sum += x
    print("Sum:", sum)

details(1, 2, 3)