'''
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
'''

import os
import math

try :
    float_num = float(input())
except:
    os._exit(1)
else:
    #math.modf分解浮点数，第一位为小数位，第二位为整数位
    if math.modf(float_num)[0] >= 0.5:
        print(int(math.modf(float_num)[1])+1)
    else:
        print(int(math.modf(float_num)[1]))
