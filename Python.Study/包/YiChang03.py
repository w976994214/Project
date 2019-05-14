import os
def func(filename):
    try:
        file = open(filename)
    except Exception as error:
        print('出错了,{}'.format(error))
    else:
        print(file.read())
        file.close()

func('hahahaha')
