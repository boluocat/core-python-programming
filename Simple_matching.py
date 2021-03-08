#朴素匹配模式
'''pos：第pos个字符之后开始匹配
'''
def Simple_matching(str1,str2,pos):
    n = len(str1)
    m = len(str2)
    i = pos
    j = 0  #python中字符串是从0位开始标记
    while i < n and j < m:
        if str1[i] == str2[j]:
            i = i + 1
            j = j + 1
        else:
            i = i - j + 1  #python中字符串是从0位开始标记，所以此处只减1
            j = 0
            #print(i)
    #print(i,j)
    if j > m - 1 :  #python中字符串是从0位开始标记，所以此处减1
        return i - m
    else:
        return 0

#str1=input('给出str2:')
#str2=input('给出str2:')
#pos=int(input('给出pos值:'))
#print(Simple_matching(str1,str2,pos))