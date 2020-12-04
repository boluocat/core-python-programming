'''
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10; A1A; $%$; YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
\+  A10  = （-10,0）
\+  S20  = (-10,-20)
\+  W10 = (-10,-10)
\+  D30 = (20,-10)
\+  x  = 无效
\+  A1A  = 无效
\+  B10A11  = 无效
\+ 一个空 不影响
\+  A10 = (10,-10)
结果 （10， -10）
'''
#code 1:通过正则匹配，一定要规划好匹配的正则有哪些，否则容易遗漏
import re
src_list = input().split(';')
src_list_1 = []
a = 0
b = 0

ARegex = re.compile(r'A\d\d')
SRegex = re.compile(r'S\d\d')
DRegex = re.compile(r'D\d\d')
WRegex = re.compile(r'W\d\d')
A_1Regex = re.compile(r'A\d')
S_1Regex = re.compile(r'S\d')
D_1Regex = re.compile(r'D\d')
W_1Regex = re.compile(r'W\d')

for i in src_list:
    if (ARegex.search(i) or WRegex.search(i) or SRegex.search(i) or DRegex.search(i) or A_1Regex.search(i) or W_1Regex.search(i) or S_1Regex.search(i) or D_1Regex.search(i) ) and (len(i) > 1 and len(i) <= 3):
        c = len(i)
        if ARegex.search(i) or A_1Regex.search(i):
            a = a - int(i[1:c])
        elif DRegex.search(i) or D_1Regex.search(i):
            a = a + int(i[1:c])
        elif WRegex.search(i) or W_1Regex.search(i):
            b = b + int(i[1:c])
        elif SRegex.search(i) or S_1Regex.search(i):
            b = b - int(i[1:c])

print('%s,%s '%(a,b))

#code 2:#通过字符串切片匹配对应的格式会更快一点
src_list = input().split(';')
a ,b = 0,0

for i in src_list:
    if i[0:1] in ['A','D','W','S'] and i[1:].isdigit() and len(i)>1 and len(i)<=3:
        c = len(i)
        if i[0:1] == 'A':
            a = a - int(i[1:c])
        elif i[0:1] == 'D':
            a = a + int(i[1:c])
        elif i[0:1] == 'W':
            b = b + int(i[1:c])
        elif i[0:1] == 'S':
            b = b - int(i[1:c])

print('%s,%s '%(a,b))
