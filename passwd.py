password = 'a123456'
x = 3
while True:
    passwd = input('請輸入密碼： ')
    if passwd == password:
        print('登入成功')
        break
    else:
        x = x - 1
        if x == 0:
            print('錯誤次數過多，系統關閉！')
            break
        print('密碼錯誤，還有 ',x,' 次機會！')
