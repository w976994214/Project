class changdu(Exception):
    def __init__(self,str1):
        self.str1 = str1
    def process(self):
        if len(self.str1) < 5:
            print('长度小于5')
        else:
            print(len(self.str1))

try:
    er = changdu('assaaaas')
    er.process()
except changdu as error:
    print(error)