# @Author: wjn
# @Time: 2019-07-24 22:23

baoding = ['安新县','雄县','容城县','返回上一级']
shijiazhuang = ['石家县','国际庄县','返回上一级']
sanhe = ['燕郊县','香河县','大厂县','返回上一级']
hebei = {'保定市':baoding,'石家庄市':shijiazhuang,
             '三河市':sanhe,'返回上一级':{}}

henan = {'郑州市','洛阳市'}
beijing = {'北京市'}
tb = {'河北省':hebei,'河南省':henan,'北京市':beijing}
quit_flag = True
while quit_flag:
    for i,j in enumerate(list(tb.keys())):
        print(i+1,j)
    first_choice = input('请选择您所在的省份(退出q):')
    location = []
    if first_choice.isdigit():
        first_choice = int(first_choice)
        if first_choice==1:
            location.append('河北省')

            while quit_flag:
                for i, j in enumerate(list(tb['河北省'].keys())):
                    print(i + 1, j)
                second_choice = input('请选择您所在的城市(退出q):')
                if second_choice.isdigit():
                    second_choice = int(second_choice)
                    if second_choice==1:
                        location.append('保定市')
                        while quit_flag:
                            for i, j in enumerate(baoding):
                                print(i + 1, j)
                            third_choice = input('请选择您所在的县(退出q):')
                            if third_choice.isdigit():
                                if third_choice=='1':
                                    location.append('安新县')
                                    print('您所在位置:',end='')
                                    # for i in location:
                                    #     print(i,end='>>>')
                                    print('{0}>>>{1}>>>{2}'.format(
                                        location[0],location[1],location[2]))
                                    quit_flag = False
                                    break
                                elif third_choice=='2':
                                    location.append('雄县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice=='3':
                                    location.append('容城县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice=='4':
                                    location.pop(1)
                                    break
                                else:
                                    print('您输入的县无效，请重新输入！')
                            elif third_choice=='q':
                                quit_flag = False
                                break
                            else:
                                print('输入无效，请重新输入！')
                    elif second_choice==2:
                        location.append('石家庄市')
                        while quit_flag:
                            for i, j in enumerate(shijiazhuang):
                                print(i + 1, j)
                            third_choice = input('请选择您所在的县(退出q):')
                            if third_choice.isdigit():
                                if third_choice == '1':
                                    location.append('石家县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice == '2':
                                    location.append('国际庄县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice == '3':
                                    location.pop(1)
                                    break
                                else:
                                    print('您输入的县无效，请重新输入！')
                            elif third_choice == 'q':
                                quit_flag = False
                                break
                            else:
                                print('输入无效，请重新输入！')
                    elif second_choice==3:
                        location.append('三河市')
                        while quit_flag:
                            for i, j in enumerate(baoding):
                                print(i + 1, j)
                            third_choice = input('请选择您所在的县(退出q):')
                            if third_choice.isdigit():
                                if third_choice == '1':
                                    location.append('燕郊县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice == '2':
                                    location.append('香河县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice == '3':
                                    location.append('大厂县')
                                    print('您所在位置:', end='')
                                    for i in location:
                                        print(i, end='>>>')
                                    quit_flag = False
                                    break
                                elif third_choice == '4':
                                    location.pop(1)
                                    break
                                else:
                                    print('您输入的县无效，请重新输入！')
                            elif third_choice == 'q':
                                quit_flag = False
                                break
                            else:
                                print('输入无效，请重新输入！')
                    elif second_choice==4:
                        location.pop(0)
                        break
                    else:
                        print('您输入的城市无效，请重新输入！')
                elif second_choice=='q':
                    quit_flag = False
                    break
                else:
                    print('输入无效，请重新输入！')
        elif first_choice==2:
            pass
        elif first_choice==3:
            pass
        else:
            print('您输入的省份无效，请重新输入！')
    elif first_choice=='q':
        break
    else:
        print('输入无效，请重新输入！')