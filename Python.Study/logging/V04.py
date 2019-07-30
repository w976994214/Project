"""
用logging的四大组件来实现日志的功能
打印出函数的执行时间，日志的等级，日志的消息
用装饰器
不同的日志，需要记录不同等级的日志消息
"""

import logging
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# handler
# TimeRotationFileHandler是用来按照日期去划分日志
# RotationFileHandler是按照日志文件的大小划分日志
debug_handler = logging.FileHandler("1024debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handler = logging.FileHandler("1024error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(debug_handler)
logger.addHandler(error_handler)


def log(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            logging.error(text)
            logging.debug(text)
            return func(*arg, **kw)
        return wrapper
    return decorator


@log("test done")
def test():
    print("test done")


@log("test done")
def main():
    print("main done")


test()
main()
