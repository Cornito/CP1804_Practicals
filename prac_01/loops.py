for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()


for i in range(20, 0, -1):
    print(i, end=' ')

print()

stars = int(input("please enter number"))

for i in range(1, stars + 1):
    print("*" * i)