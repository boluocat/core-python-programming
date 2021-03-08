#KMP
'''求解next数组，假设字符串为i个元素
比较字符串0到i-1的串的前缀数组和后缀数据的相同项
1、i=0时，next[i]=0
2、i=1时，next[i]=1
3、i>=2，且2到i-1的串的前缀数组和后缀数据存在相同项，next[i]=max(相同字符长度)
4、其他，next[i]=1
'''
def next_list(str2):
    next_list , ys= [],[]
    for i in range(0,len(str2)):
        #print('--->',str2[0:i])
        if i == 0:
            next_list.append(0)
        elif i == 1:
            next_list.append(1)
        else:
            for j in range(0,i-1):
                str_prefix = str2[0:i][:j+1]  #前缀，B+S
                str_suffix = str2[0:i][-j-1:] #后缀，S+B
                #print(str_prefix,str_suffix)
                if str_suffix == str_prefix:
                    ys.append(len(str_prefix)+1)
                else:
                    ys.append(1)
                #print(ys)
            next_list.append(max(ys))
            ys.clear()
    return next_list

'''借用前一个字符的判断结果，计算当前字符对应的 next 值
'''
def next_list_1(str2):
    next_list = []
    i = 1
    j = 0
    next_list.append(0)
    while i < len(str2):
        if j == 0 or (str2[i-1] == str2[j-1]):
            i = i + 1
            j = j + 1
            next_list.append(j)
        else:
            j = next_list[j-1]
    return next_list


def nextval(str2):
    nextval_list = []
    i = 1
    j = 0
    nextval_list.append(0)
    while i < len(str2):
        if j == 0 or (str2[i-1] == str2[j-1]):
            i = i + 1
            j = j + 1
            if str2[i-1] != str2[j-1]:
                nextval_list.append(j)   #不相等，则将j值赋予nextval,等同于nextval[j]=next[j]
            else:
                nextval_list.append(nextval_list[j-1])  #相等，则将前一个nextval值赋予当次的nextval。等同于nextval[j] = nextval[next[j]-1] 
        else:
            j = nextval_list[j-1]
    return nextval_list

        
def KMP_matching(str1,str2,pos):
    n = len(str1)
    m = len(str2)
    i = pos
    j = 0  #从0位开始标记
    next = nextval(str2)
    while  i < n and j < m:
        if j == -1 or str1[i] == str2[j]:
            i = i + 1
            j = j + 1
        elif str1[i] != str2[j]:
            if j == 0:  #在字符匹配不相等的情况下，子串如果回到了首位，则表示重新开始匹配，需要主串移动一位
                j = 0
                i = i+1
            else:
                j = next[j-1]  
    if j > m - 1 : 
        return i - m
    else:
        return 'None'

str1=input('给出str1:')
str2=input('给出str2:')
pos=int(input('给出pos值:'))
print(KMP_matching(str1,str2,pos))