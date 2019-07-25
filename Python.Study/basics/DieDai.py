num = int(input('shusru'))

ci = 0

def jisuan(num):
    global ci

    while num != 1:

        if num % 2 == 0:
            num /= 2
            ci += 1
        else:
            num = num * 3 + 1
            ci += 1


    print(ci)

jisuan(num)