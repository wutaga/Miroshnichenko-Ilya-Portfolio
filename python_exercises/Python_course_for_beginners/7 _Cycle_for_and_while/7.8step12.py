total = 0
for t in range(1, 201):
    for k in range(1, 21):
        for b in range(1, 11):
            if 10*b+5*k+0.5*t == 100 and t+k+b == 100:
                total += 1
                print('t =', t, 'k =', k, "b =",b)
print(total)