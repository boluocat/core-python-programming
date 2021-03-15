class Nodes:
    #结点生成，先初始化
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None
 

class BiTree:
    #初始化root为None
    def __init__(self,node=None):
        self.root = node
    
    def addnode(self,item):
        #如果根节点为None，则将第一个接收到的值赋给根结点
        if self.root is None:
            self.root = Nodes(item)
        else:
            #否则将其添加到结点列表中，作为子结点
            nodelist = list()
            nodelist.append(self.root)
            while len(nodelist) > 0:
                node = nodelist.pop(0)
                #先添加左子树
                if not node.lchild:
                    node.lchild = Nodes(item)
                    return
                else:
                    nodelist.append(node.lchild)

                #再添加右子树
                if not node.rchild:
                    node.rchild = Nodes(item)
                    return
                else:
                    nodelist.append(node.rchild)


    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

 
class SearchTree:
    '''以下方法都定义了return值。
       如果不定义return值，在调用该方法再一次进行print，则末尾会打印出一个多余的None值。
       相当于程序自动在末尾添加了一个 return None，所以需要指定返回值
    '''

    #使用list将结果存储起来，初始化的时候定义一下
    def __init__(self):
        self.preorder = []
        self.inorder = []
        self.postorder = []

    #前序
    def preorder_travel(self, root):
        if root is not None:
            self.preorder.append(root.item)
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild) 
        return self.preorder  

    #中序
    def inorder_travel(self, root):
        if root is not None:
            self.inorder_travel(root.lchild)
            self.inorder.append(root.item)
            self.inorder_travel(root.rchild)
        return self.inorder
        
    #后序
    def postorder_travel(self, root):
        if root is not None :
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            self.postorder.append(root.item)
        return self.postorder

if __name__ == '__main__':
    tree = BiTree()
    node_data = input('输入树的结点数据：').split(',')
    for i in node_data:
        tree.addnode(i)
    
    #print(tree.root.lchild.rchild.item)
    #print(tree.root.lchild.lchild.rchild.item)

    nodes = SearchTree()
    print(nodes.preorder_travel(tree.root))
    print(nodes.inorder_travel(tree.root))
    print(nodes.postorder_travel(tree.root))