# @Author: wjn
# @Time: 2019-07-20 22:21

salary = int(input('请输入您现在有多少钱：'))
balance = salary
price_iphone7 = 5800
price_coffee = 33
price_py_book = 400
price_bicyle = 1500
price_macbook = 4000

price_list = [price_iphone7, price_coffee, price_py_book, price_bicyle, price_macbook]
name_list = ['iphone7','coffee','python book','bicyle','macbook']
buy_list = []

print('''
商品列表：
1.iphone7 %d
2.coffee %d
3.python book %d
4.bicyle %d
5.macbook %d
'''%(price_iphone7,price_coffee,price_py_book,price_bicyle,price_macbook))


while True:
    choice = input('加入购物车的物品>>>:')

    if choice == 'quit':
        print('您已购买以下商品：')
        for j in buy_list:
            # print(j + '>>>' + str(price_list[name_list.index(j)]))
            print('%s >>> %d'%(j,price_list[name_list.index(j)]))
        print('欢迎下次光临\n您的余额是：%d'%balance)
        break
    elif balance - price_list[int(choice)-1] < 0:
        print('余额不足，',balance - price_list[int(choice)-1])
    else:
        
        buy_list.append(name_list[int(choice)-1])
        balance = balance - price_list[int(choice)-1]
        print('已将%s 加入购物车，当前余额：%d'%(name_list[int(choice)-1],balance))