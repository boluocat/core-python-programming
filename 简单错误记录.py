'''
1、 记录最多8条错误记录，循环记录，最后只用输出最后出现的八条错误记录。对相同的错误记录只记录一条，但是错误计数增加。最后一个斜杠后面的带后缀名的部分（保留最后16位）和行号完全匹配的记录才做算是”相同“的错误记录。
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。
4、循环记录时，只以第一次出现的顺序为准，后面重复的不会更新它的出现时间，仍以第一次为准
每组只包含一个测试用例。一个测试用例包含一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：
D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
E:\je\rzuwnjvnuz 633
C:\km\tgjwpb\gy\atl 637
F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
E:\ns\mfwj\wqkoki\eez 648
D:\cfmwafhhgeyawnool 649
E:\czt\opwip\osnll\c 637
G:\nt\f 633
F:\fop\ywzqaop 631
F:\yay\jc\ywzqaop 631

输出：
rzuwnjvnuz 633 1
atl 637 1
rwyfvzsopsuiqjnr 647 1
eez 648 1
fmwafhhgeyawnool 649 1
c 637 1
f 633 1
ywzqaop 631 2
'''

#code
'''
使用字典进行唯一性的保障，用截取后的路径字符与行数作为key值，统计个数作为value值。
最后将迭代的字典转换为数组，输出后8位元素
'''
dic = {}
log_list = []
while True:
    try:
        dir,lines = input().split(' ')
        dir = dir.split('\\')[-1]
        if len(dir)<=16:
            keys = dir + ' ' + lines
        else:
            keys = dir[-16:] + ' ' + lines
        dic[keys] = dic.get(keys,0) + 1
    except :
        break

for i,j in dic.items():
    logs = str(i)+' '+str(j)
    log_list.append(logs)

if len(log_list) >= 8:
    for log_value in log_list[-8:]:
        print(log_value)
else:
    for log_value in log_list:
        print(log_value)
