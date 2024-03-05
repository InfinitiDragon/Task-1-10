n = int(input("Введіть значення n: "))
m = int(input("Введіть порядковий номер студента у журналі: "))

for i in range(-n, n+1, m):
    if i % 2 == 0:
        print(i)
8