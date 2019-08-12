"""
使用协程概念计算abcd四个整数，打印除（a+b）*（c+d），假设+计算耗时1S
"""
import asyncio
import threading


async def sum1(a, b):
    print("准备开始计算,current thread is {}".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("计算完成，current thread is {}".format(threading.currentThread()))
    return r

loop = asyncio.get_event_loop()
task = asyncio.gather(sum1(1, 2), sum1(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1)*int(r2))
loop.close()