# @Author: wjn
# @Time: 2019-08-10 21:29

import re
import math
s = '1 - 2 * ( (60 -30 + (-40.2/-5.5) * (9-2*5/3 + 7 /3 *99/4*2998 + ' \
    '10 * 568/14))  -(-4*3) / (16 - 3*2)  )'

s = re.sub(' +','',s)
# print(s)
while True:

    ret = re.search('\([^()]+\)',s)
    if ret is not None:
        print(ret.group()[1:-1])
        if re.search('-?\d*\.?\d+[*,/]-?\d*\.?\d+',ret.group()[1:-1]):
            chengchu = re.search('-?\d*\.?\d+[*,/]-?\d*\.?\d+',ret.group()[1:-1]).group()
            print('wwww',chengchu)
            if re.search('\*',chengchu):
                chengchu_after = re.split('[*,/]', chengchu)
                print('dddd',chengchu_after)
                res = round(float(chengchu_after[0]) * float(chengchu_after[1]),2)
                print('res:',res)
                # ret.group()[1:-1] = ret.group()[1:-1].replace(chengchu,str(res))
                # print(ret.group()[1:-1])
                # res = s.replace(ret.group(), str(res))
                s = s.replace(re.search('-?\d*\.?\d+[*,/]-?\d*\.?\d+',ret.group()).group(),str(res))
                print(s)
                if '-+' in s:
                    s = s.replace('-+', '-')
                elif '+-' in s:
                    s = s.replace('+-', '-')
                print(s)
            elif re.search('/',chengchu):
                chengchu = re.split('[*,/]', chengchu)
                print('wwwww-chengchu:',chengchu)
                res = round(float(chengchu[0]) / float(chengchu[1]),2)
                print('qqq-res:',res)
                s = s.replace(re.search('-?\d*\.?\d+[*,/]-?\d*\.?\d+',ret.group()).group(),str(res))
                print(s)
                if '-+' in s:
                    s = s.replace('-+', '-')
                elif '+-' in s:
                    s = s.replace('+-', '-')
                print(s)
            # break
        elif re.search('-?\d*\.?\d+[+,\\-]-?\d*\.?\d+',ret.group()[1:-1]):
            chengchu = re.search('-?\d*\.?\d+[+,\\-]-?\d*\.?\d+', ret.group()[1:-1]).group()
            print('test',chengchu)
            if re.search('\d+\+',chengchu):
                chengchu = re.split('[+,\\-]', chengchu)
                res = round(float(chengchu[0]) + float(chengchu[1]),2)
                s = s.replace(ret, str(res))
                print(s)
            elif re.search('\d+-',chengchu):
                chengchu = re.split('[\+,-]', chengchu)
                print(chengchu)
                if len(chengchu) == 3:
                    chengchu.remove('')
                    res = round(-float(chengchu[0]) - float(chengchu[1]),2)
                    s = s.replace(ret.group(),str(res))
                    if '-+' in s:
                        s = s.replace('-+','-')
                    elif '+-' in s:
                        s = s.replace('+-','-')
                    print(s)
                elif len(chengchu) == 2:
                    res = round(float(chengchu[0]) - float(chengchu[1]), 2)
                    s = s.replace(ret.group(), str(res))
                    print(s)
            # break
    else:
        break
