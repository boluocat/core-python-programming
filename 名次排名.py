'''
有M个裁判（3<M<10），N个选手(3<N<10)。每个裁判依次给选手打分(最高为10分)。当比赛结束后，按照选手的总分进行名次排序，选前三名输出(如果选手总分一样的情况下，比较所得分值，例如A选手2个9分，B选手3个9分，则B名次高于A)。
输入：
1、第一行为裁判数、选手数，用英文逗号分隔
2、第二行至第j行为第j+1个裁判打出的分数，从左至右依次为第一位选手至第n位选手的分数
输出：
1、当M或N小于3时，输出-1；
2、当裁判所给分数>10时，输出-1；
3、输出前面前三的选手序号

#输入
4,5
10,6,9,7,6
9,10,6,7,5
8,10,6,5,10
9,10,8,4,9
#输出
2,1,5
'''
import os

M,N = map(int,input().split(','))
dic_scoreclass_count = {}
dic_score_num = {}
dic_temp = {}
score_list = []
ranking_list = []
scoreclass_count_list  = []
output = ''


if (M >10 or M<3)  or (N >10 or N<3):
    print('-1')
else:
    for i in range(M):
        line = input().split(',')
        for j in line:
            if int(j) > 10:
                print('-1')
                os._exit(2)
        else:
            score_list.append(line)
    
def tr(alist):
    tr_list = []
    for i in range(len(alist[0])):
        temp = []
        for j in range(len(alist)):
            temp.append(alist[j][i])
        tr_list.append(temp)
    return tr_list

def count_n(slist,kw):
    num = slist.count(kw)
    return num 

def get_keys(sdic,values):
    return [k for k,v in sdic.items() if v == values]

personal_score_list =  tr(score_list)
for k in personal_score_list:
    temp_list = []
    v = 0
    for g in k:
        v = v + int(g)
    temp_list.append(v)
    for h in range(10):
        temp_list.append(count_n(k,str(h+1)))
    scoreclass_count_list.append(temp_list)

for i in range(len(scoreclass_count_list)):
    dic_scoreclass_count[i+1] = scoreclass_count_list[i][0]
    counter = 0
    for j in scoreclass_count_list[i][1:]:
        if j > 0 :
            counter = counter + 1
    dic_score_num[i+1] = counter

for i in range(3):
    top3_sccount = get_keys(dic_scoreclass_count,sorted(dic_scoreclass_count.values(),reverse=True)[0:3][i])
    top3_len = len(top3_sccount)

    if top3_len > 1:
        for j in top3_sccount:
            dic_temp[j] = dic_score_num[j]
        ranking_list.append(sorted(dic_temp.items(),key = lambda item:item[1]))
    else:
        if len(ranking_list) > 0 :
            inttop3_sccount = int(''.join(map(str,top3_sccount)))
            if type(ranking_list[i-1]) == list:
                ranking_list[top3_len-1].append((inttop3_sccount,dic_score_num[inttop3_sccount]))
            elif type(ranking_list[i-1]) == tuple:
                ranking_list.append((inttop3_sccount,dic_score_num[inttop3_sccount]))
                
        else:
            inttop3_sccount = int(''.join(map(str,top3_sccount)))
            ranking_list.append((inttop3_sccount,dic_score_num[inttop3_sccount]))

if len(ranking_list[0]) == 3:
    for i in ranking_list[0]:
        output = output + str(i[0]) + ','
    print(output[0:len(output)-1])
else:
    for i in ranking_list:
        output = output +str(i[0]) + ','
    print(output[0:len(output)-1])
