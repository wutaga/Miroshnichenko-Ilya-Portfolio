a, b = int(input()), int(input())
total = 0
for i in range(a, b):
    if i ** 3 % 4 == 0 or i ** 3 % 9 == 0:
        total += 1
print(total)
