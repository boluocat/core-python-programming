'''
检测是否为回文串，如果一个字符串从左往右和从右向左读取是完全相同的，则称为回文串
noon,madam
'''

'''递归
如果字符串长度等于1，是回文串
否则，s[0]==s[n],s[1]==s[n-1]...
直到低位大于高位为止
'''
def palindrome_recursion(instr,l,h):
    instr_lower = instr.lower()
    if l > h:
        return 1
    elif len(instr_lower) > 1:
        if instr_lower[l]== instr_lower[h]:
            return palindrome_recursion(instr_lower,l+1,h-1)
        else:
            return 0
    else:
        return 1

'''迭代
如果字符串长度等于1，是回文串
'''
def palindrome_interation(instr):
    instr_lower = instr.lower()
    m = len(instr_lower)
    if m > 1:
        for i in range(0,m-1):
            if  i > m-i-1:
                return 1
            elif instr_lower[i] == instr_lower[m-1-i]:
                continue
            else:
                return 0
    else:
        return 0
    
instr = 'knolonK'
l = 0
h = len(instr)-1
print('递归结果为：{}'.format(palindrome_recursion(instr,l,h)))
print('迭代结果为：{}'.format(palindrome_interation(instr)))