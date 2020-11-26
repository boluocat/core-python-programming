'''
  手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，以此规则试设计一个程序，将单词用一串数字来进行表示。 
 For example:
 输入：cat（不区分大小写） 
 输出：228
'''
word = input()
result = []

for i in range(len(word)):
    o = ord(word[i].upper())
    if o >= 65 and o <=67:
        result.append('2')
    elif o >= 68 and o <=70:
        result.append('3')
    elif o >= 71 and o <=73:
        result.append('4')
    elif o >= 74 and o <=76:
        result.append('5')
    elif o >= 77 and o <=79:
        result.append('6')
    elif o >= 80 and o <=82:
        result.append('7')
    elif o >= 83 and o <=85:
        result.append('8')
    else:
        result.append('9')
print(''.join(result))
