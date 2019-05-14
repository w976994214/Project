def jianfa(A,B):
    if A < B:
        raise BaseException('A小于B')
    else:
        return A-B
try:
    jianfa(3,7)
except BaseException as error:
    print('出错了,{}'.format(error))