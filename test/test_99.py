n1 = 1
while n1 <= 9:
    n2 = 1
    while n2 <= n1:
        # print(str(n1) + '*' + str(n2) + '=' + str(n1 * n2), end=' ')
        print('%d*%d=%d'%(n1,n2,n1*n2),end=' ')
        n2 += 1
    n1 += 1
    print()