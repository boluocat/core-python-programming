'''
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
所有的IP地址划分为 A,B,C,D,E五类
A类地址1.0.0.0~126.255.255.255;
B类地址128.0.0.0~191.255.255.255;
C类地址192.0.0.0~223.255.255.255;
D类地址224.0.0.0~239.255.255.255；
E类地址240.0.0.0~255.255.255.255

私网IP范围是：
10.0.0.0～10.255.255.255
172.16.0.0～172.31.255.255
192.168.0.0～192.168.255.255

子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.】和【127.*.*.】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入：
多行字符串。每行一个IP地址和掩码，用~隔开。
输出：
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''

#code
'''
A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数.
坑点1：IP和掩码要同时合法才能算记作正常的类别，如果有一个不合法则都归于不合法类
坑点2：掩码转换为二进制时要考虑不足8位的情况，需要补齐
坑点3：'0.x.x.x'和'127.x.x.x'也需要判断掩码是否正常，只是忽略了IP而已
坑点4：公网IP和私网IP不冲突，需要同时归属
'''

a,b,c,d,e,err,private_ip = 0,0,0,0,0,0,0

def err_ip(list):
    for i in list:
        if len(i)==0  or int(i) > 255 or int(i) < 0:
            return True

def privateip(list):
    if int(list[0]) == 10 and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return True
    elif int(list[0]) == 172 and (int(list[1]) >=16 and int(list[1])<=31) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return True
    elif int(list[0]) == 192 and int(list[1]) ==168  and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return True
    else:
        return False

def ipclass(list):
    if (int(list[0]) >= 1 and int(list[0])<= 126) and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return 'A'
    elif (int(list[0]) >= 128 and int(list[0])<=191) and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return 'B'
    elif (int(list[0]) >= 192 and int(list[0])<=223) and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return 'C'
    elif (int(list[0]) >= 224 and int(list[0])<=239) and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return 'D'
    elif (int(list[0]) >= 240 and int(list[0])<=255) and (int(list[1]) >=0 and int(list[1])<=255) and (int(list[2]) >=0 and int(list[2])<=255) and (int(list[3]) >=0 and int(list[3])<=255):
        return 'E'

def err_mask(list):
    a = ''
    b = 0
    for i in list:
        bin_value = bin(int(i,10))[2:]
        if len(bin_value) < 8:
            a = a + '0'*(8 - len(bin_value))+bin_value
        else:
            a = a + bin_value
    for j in a.split('0')[1:]:
        if j == '':
            b = b + 0
        else:
            b = b + int(j)
    if list == ['255','255','255','255'] or list == ['0','0','0','0'] or b > 0:
        return True
    else:
        return False
    
while True:
    try:
        ip,mask = input().split('~')
        ip_list = ip.split('.')
        mask_list = mask.split('.')
            #IP判断
        if (ip_list[0] == '0' or ip_list[0] == '127') and err_mask(mask_list) == False:  #特殊部分排除
            pass
        elif  (ip_list[0] == '0' or ip_list[0] == '127') and err_mask(mask_list) == True:
            err = err + 1
        elif err_ip(ip_list) == True or err_mask(mask_list) == True: #错误判断
            err = err + 1
        else:
            if ipclass(ip_list) == 'A':
                a = a + 1
            if ipclass(ip_list) == 'B':
                b = b + 1
            if ipclass(ip_list) == 'C':
                c = c + 1 
            if ipclass(ip_list) == 'D':
                d = d + 1
            if ipclass(ip_list) == 'E':
                e = e + 1
            if privateip(ip_list) == True:
                private_ip = private_ip + 1

    except :
        break
print(a,b,c,d,e,err,private_ip)
