'''
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
输入一个long型整数,按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''

def pro(int_num):
    num = int(int_num)
    #使用列表进行结果记录，方便结果转换后在一行输出
    a_list = list()
    s = 2 #以2作为起始点
    while True:
        #如果能整除，将除数加入list,并更新被除数
        if num % s == 0:
            a_list.append(str(s))
            num = num // s
        #如果除数的平方被除数，本次被除数，停止迭代，并将被除数写入list,排除除数为1的情况
        elif s*s > num:
            if num == 1:
                break
            else:
                a_list.append(str(num))
                break
        #否则除数加一，再进入下一次循环
        else:
            s += 1
    
    #将list中的每个元素用空格进行替换，并转换为字符串，同时在最后一个字符后添加空格。待转换list中的元素应为string,所以在上面程序中做了转换。
    result = ' '.join(a_list) + ' '
    print(result)

pro(input())
