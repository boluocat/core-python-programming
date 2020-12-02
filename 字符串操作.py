'''
题目描述：给定两个字符串a b，注意：其中a字符串中有空格。求b字符串在a字符串中出现的次数。例：

输入：a="abc cc d"，b="cc"。

输出：b在a中出现次数为：2次
'''

a = ''.join(input().split())
b = input()
a_len = len(a)
b_len = len(b)
c = 0

if b_len > a_len:
    print(0)
else:
    for i in range(a_len-b_len+1):
        if b in a[i:i+b_len]:
            c = c+1
    print(c)
