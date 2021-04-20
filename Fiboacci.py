'''递归 recursion
'''

def Fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return Fibonacci_recursion(n-1)+Fibonacci_recursion(n-2)

'''迭代 iteration
前一个数字+当前数值=下一个数值
'''
def Fibonacci_interation(n):
    if n ==0 :
        return 0
    elif n == 1:
        return 1
    else:
        now = 1
        pre = 0
        for j in range(2,n+1):
            next = pre + now
            pre = now
            now = next
        return next

sp = 0
ep = 10
Fibonacci_recursion_list = []
Fibonacci_interation_list = []

while sp <= ep:
    fibonacci_recursion = Fibonacci_recursion(sp)
    fibonacci_interation = Fibonacci_interation(sp)
    sp += 1
    Fibonacci_recursion_list.append(fibonacci_recursion)
    print('----------------------------------->')
    print('sp = {}, Fibonacci = {}'.format(sp,fibonacci_recursion))
    Fibonacci_interation_list.append(fibonacci_interation)
    print('sp = {}, Fibonacci = {}'.format(sp,fibonacci_interation))    
print(Fibonacci_recursion_list)
print(Fibonacci_interation_list)