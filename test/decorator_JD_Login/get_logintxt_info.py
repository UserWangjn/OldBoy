# @Author: wjn
# @Time: 2019-08-05 13:10

def get_username():
    username = []
    with open('jd_login.txt') as jd:
        line = 1
        for i in jd:
            # print(i)
            if line%3 == 1:
                username.append(i[i.find('=')+1:i.find('\n'):])
            line += 1
    return username

print(get_username())