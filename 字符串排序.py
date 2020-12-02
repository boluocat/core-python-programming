'''
给定n个字符串，请对n个字符串按照字典序排列。
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
数据输出n行，输出结果为按照字典序排列的字符串。
'''


a = int(input())
b = []
#读取所有input
for i in range(a):
    b.append(input())
#直接获取list元素进行打印
for j in sorted(b):
    print(j)
