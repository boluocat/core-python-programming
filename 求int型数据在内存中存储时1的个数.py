'''
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
'''

a = bin(int(input()))
b = a.count('1')
print(b)
