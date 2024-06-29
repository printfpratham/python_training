y = []
z = []
print("Enter item to add in a list")
for i in range(0,5):
    x = input()
    y.append(x)

print(y)

x = input("Enter item to remove: ")
if x in y:
    z.append(x)
    y.remove(x)
    print(y)
    print(z)
else:
    print("Item does not exist")
