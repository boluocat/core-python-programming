'''
顶点数据 a,b,c,d
如果有权值，邻接矩阵中使用权值，0，65535表示；如果无权值，则用0，1表示
起始顶点,到达顶点,权值   例如：a-b,b-c,c-d  a-b-2,b-c-3,c-d-4
是否为无向图 0，1
'''
def CreateMGraph(vertices,arc_w_list,Gtpye,wtype):
    vertices_list = vertices #创建顶点数组
    n = len(vertices_list) #计算顶点数
    #初始化边数矩阵,[[0]*n]*n无法给特定位置的元素赋值
    arc_list_0 = [[0]*n for i in range(n)]
    arc_list_1 = [[65535]*n for i in range(n)]
    #标记顶点元素的下标
    vertices_index,k = {},0
    for p in vertices:
        vertices_index[p] = k
        k += 1

    #填充边矩阵
    if wtype == 0:
        if Gtpye == 0:
            print('该图为无向无权图')
            for s in arc_w_list:
                i,j = vertices_index[s[0]],vertices_index[s[1]]
                #对称填充
                arc_list_0[i][j],arc_list_0[j][i] = 1,1
        elif Gtpye == 1:
            print('该图为有向无权图')
            for s in arc_w_list:
                i,j = vertices_index[s[0]],vertices_index[s[1]]
                #非对称填充
                arc_list_0[i][j] = 1
        return vertices_list,arc_list_0
    elif wtype == 1:
        for g in range(len(vertices_list)):
            arc_list_1[g][g] = 0
        if Gtpye == 0:
            print('该图为无向有权图')
            for s in arc_w_list:
                i,j,w_value = vertices_index[s[0]],vertices_index[s[1]],int(s[2])
                #对称填充
                arc_list_1[i][j],arc_list_1[j][i] = w_value,w_value
        elif Gtpye == 1:
            print('该图为有向有权图')
            for s in arc_w_list:
                i,j,w_value = vertices_index[s[0]],vertices_index[s[1]],int(s[2])
                #非对称填充
                arc_list_1[i][j] = w_value
        return vertices_list,arc_list_1
    else:
        print('error')


Gtpye,vertices,arc_w = int(input('输入图的类型，1代表有向图，0代表无向图：')),input('输入顶点信息：').split(','),input('输入边的信息,为引号内格式"起始顶点-到达顶点-权值"：').split(',')
arc_w_list,wv = [],0
for w  in range(0,len(arc_w)):
    sub_arc = arc_w[w].split('-')
    arc_w_list.append(sub_arc)
    if len(sub_arc) == 2:
        wv += 0
    elif len(sub_arc) == 3:
        wv += 1
    else:
        break
if wv == len(arc_w_list):
    wtype = 1
elif wv == 0:
    wtype = 0
else:
    print('所有边没有统一携带/未携带权值')

VerticesList,ArcList = CreateMGraph(vertices,arc_w_list,Gtpye,wtype)
print('顶点数组为:%s,边数组为：%s'%(VerticesList,ArcList))