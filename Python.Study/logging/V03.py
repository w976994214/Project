"""
装饰器
使用装饰器打印函数执行的时间

使用装饰其根据不同的函数，传入的日志不相同
"""

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT)


def log(test):
    def decorator(func):
        def wrapper(*arg, **kw):
            logging.error(test)
            return func(*arg, **kw)
        return wrapper
    return decorator


@log("test done")
def test():
    print("test done")


@log("main done")
def main():
    print("main done")


test()
main()
