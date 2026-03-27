tuple = ("abcd", 786, 2.23)
list = ["abcd", 786, 2.23]

list[0] = 1000
print(list)
# deliberate error here
tuple[0] = 1000
print(tuple)