# @Author: wjn
# @Time: 2019-07-27 23:31

# with open('test_file.txt','w') as f:
#     f.writelines('hello world\nthis is a file test!\na nice day')
row = 0
with open('test_file.txt','r') as f, open('test_file_copy.txt','w') as ff:
    for i in f:
        line = i
        row += 1
        if row == 2:
            line = ''.join([i.strip(),'good study~\n'])
        ff.writelines(line)