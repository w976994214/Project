# 关于concurrent案例
from concurrent.futures import ThreadPoolExecutor
import time


def return_future(msg):
    time.sleep(3)
    return msg


# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)

# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')

# 等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())

# 结果
print(f1.result())
print(f2.result())

# 输出结果
False
False
hello
world