import random

a = random.randint(0, 100)

b = random.randint(0, 100)

if b > a:
    print("Le nombre b est plus grand que le nombre a.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else:
    print("Le nombre a et le nombre b sont égaux.")