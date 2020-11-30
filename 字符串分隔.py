'''
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
连续输入字符串(输入多次,每个字符串长度小于100)
输出到长度为8的新字符串数组
'''
def case_ex(a):
    inputs,input_list=str(a),list()  
    input_list.append(inputs)
    for i in range(len(input_list)):
        key_len = len(input_list[i])
        
        if key_len < 8:
            for j in range(8 - key_len):
                input_list = input_list + ['0']
            print(''.join(input_list))
        elif key_len == 8:
            print(input_list[i])
        else:
            b = key_len // 8
            c = key_len % 8
            if c == 0:
                for k in range(b):
                    if k == 0:
                        s = k * 8
                    else:
                        s = k * 8 
                    e = k * 8 + 8
                    print(input_list[i][s:e])
            else:
                for n in range(b):
                    if n == 0:
                        s = n * 8
                    else:
                        s = n * 8 
                    e = n * 8 + 8
                    print(input_list[i][s:e])
                a = list(input_list[i][b*8:])
                for j in range(8-c):
                    a = a + ['0']
                print(''.join(a))


if __name__ == '__main__':

    while True:
        try:
            inputs = input()
            case_ex(inputs)
        except :
            break
