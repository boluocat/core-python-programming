def Permutation(result_list,input_list,k,n):
    if k < n-1:
        for i in range(k,n):
            target_list = input_list.copy()
            if  k == i:
                pass
            else:
                target_list[k] = input_list[i]
                target_list[i] = input_list[k]
                result_list.append(target_list)
            Permutation(result_list,target_list,k+1,n)
    else:
        pass
    return result_list
    
input_list = input('输入待排序数据，用逗号分隔:').split(',')
n = len(input_list)
result_list = []
Permutation(result_list,input_list,0,n)
result_list.append(input_list)
print('待排序序列为{}，可排序结果为{}'.format(input_list,result_list))
