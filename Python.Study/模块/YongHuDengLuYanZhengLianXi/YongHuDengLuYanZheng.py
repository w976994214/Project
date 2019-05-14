import os
import time
import json

count = 0

exit_flag = False

while count < 3:
    user = input("请输入用户名： ")
    f = user.strip() + '.json'
    if os.path.exists(f):
        fp = open(f, 'r+', encoding='utf-8')
        j_user = json.load(fp)
        if j_user['status'] == 1:
            print("账号已锁定")
            break
        else:
            expire_date = j_user['expire_date']
            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_date, "%Y-%m-%d"))

            if current_st > expire_st:
                print("用户已经过期")
                break
            else:
                while count < 3:
                    pwd = input("请输入密码: ")
                    if pwd.strip() == j_user["password"]:
                        print("登陆成功")
                        exit_flag = True
                        break
                    else:
                        print("密码错误，请重新输入")
                        if count == 2:
                            print("用户登录超过3次，锁定账号")
                            j_user['status'] = 1
                            fp.seek(0)
                            fp.truncate()  # 清空文件内容
                    count += 1
    if exit_flag:
        break
    else:
        print("用户不存在")
        count += 1
