a = float(input("Enter an amount: "))

if(a < 1000):
    discount = 5
elif a < 5000:
    discount = 10
else:
    discount = 15

print("Net payable:", a * ((100 - discount) / 100))