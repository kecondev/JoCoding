money = False

if money:
    print("I will buy a car")
else:
    print("I will take a bus")

if money:
    print("I will")
print("buy a car")

x = 3
y = 2
print(x == y)


a = [1, 2, 3, 4, 5]
b = 7
if b in a:
    print("b is in a")
    print("%s is in a" % b)
else:
    print(f"{b} is not in {a}")
    print("%s is not in %s" % (b, a))
