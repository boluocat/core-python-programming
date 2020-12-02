'''
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

保证输入的整数最后一位不是0。
'''

c = input()[::-1]
a = {}
d = []
for i in c:
    a[i] = a.get(i,0)

for k,v in a.items():
    d.append(k)

f = ''.join(d)
print(f)
