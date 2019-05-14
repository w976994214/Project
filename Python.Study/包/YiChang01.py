class ShouDongError(ValueError):
    pass
try:
    print('1111')
    raise ShouDongError
except NameError as e:
    print('nameerror')
except ShouDongError as e:
    print('shoudong')
except ValueError as e:
    print('valueerror')
finally:
    print('2222')