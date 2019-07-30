"""
装饰器
使用装饰器打印函数执行的时间

"""

import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=LOG_FORMAT)


def log(func):
    def wrapper(*arg, **kw):
        logging.info("info message")
        return func(*arg, **kw)
    return wrapper


@log
def test():
    print("test done")


test()
