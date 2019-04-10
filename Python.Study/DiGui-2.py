num = int(input("shuru"))
ci = 0
def jisuan(num):
    global ci
    if num == 1:
        print(ci)
        return
    else:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        ci += 1
        jisuan(num)

jisuan(num)
