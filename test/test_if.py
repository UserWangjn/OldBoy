#coding=utf-8
#@Author:Administrator
#@date:2019/11/19   11:05

score = int(input("请输入一个在 0-100 之间的数字："))
degree = "ABCDE"
num = 0
if score>100 or score<0:
    score = int(input("输入错误！请重新输入一个在 0-100 之间的数字："))
else:
    num = score//10
if num<6:num=5
print("分数是{0},等级是{1}".format(score,degree[9-num]))      # 这里有个bug,如果100分的话就会是E等级