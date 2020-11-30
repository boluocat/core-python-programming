'''
输入:数组字用英文逗号隔开。
输出:
1、选取数组中的三个数字组合成最小数输出
2、如果数组中的数字个数小于3，则采用全部数字进行组合输出，输出最小值
例如：
#输入
32,435,6,543,654
#输出
324356
'''

a = list(input().split(','))
c = sorted(map(int,a))[0:3]
d = list(map(str,c))
b = ''
e = ''
if len(a) <=3:
    for i in sorted(a):
        b = b+i
    print(b)
else:
    for j in sorted(d):
        e = e + j
    print(e)
