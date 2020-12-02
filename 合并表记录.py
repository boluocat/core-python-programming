'''
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
'''

num = int(input())
dic = {}
for i in range(num):
    line = input().split()
    key = int(line[0])
    value = int(line[1])
    #dic.get(key,0)代表如果key值不存在，则返回0，存在则返回当前对应的value值
    dic[key] = dic.get(key,0) + value

#sorted返回的是一个key值排序的list
for key in sorted(dic):
    print(key,dic.get(key))
