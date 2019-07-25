import random

x = random.randrange(1,16)
y = random.randrange(1,16)
z = random.randrange(1,16)

print(x)
print(y)
print(z)

ren = int(input('shuru'))

ceng = []

x2 = abs(x-ren)
y2 = abs(y-ren)
z2 = abs(z-ren)

ceng.append(x2)
ceng.append(y2)
ceng.append(z2)

lai = min(ceng)


if lai == x2:
    print('x')

elif lai == y2:
    print('x')

elif lai == z2:
    print('x')




