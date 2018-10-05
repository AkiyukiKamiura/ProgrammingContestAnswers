#! python3
# treap.py

class TreapNode:
    def __init__(self, left=None, right=None, val=None, priority=None):
        self.left = left
        self.right = right
        self.val = val
        self.priority = priority

class Treap:
    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        if self.root == node: self.root = node.left
        s = node.left
        node.left = s.right
        s.right = node
        return s // root of the subtree

    def left_rotate(self, node):
        if self.root == node: self.root = node.right
        s = node.right
        node.right = s.left
        s.left = node
        return s // root of the subtree

    def insert(self, key, priority):
        if self.root == None:
            self.root = TreapNode(val=key, priority=priority)
        else:
            self.__insert(self.root, key, priority)

    def __insert(self, node, key, priority):                        # 再帰的に探索
        if node == None:
            return TreapNode(val=key, priority=priority)            # 葉に到達したら新しい接点を生成して返す
        if key == node.key:
            return node                                             # 重複したkeyは無視

        if key < node.key:                                          # 左の子に移動
            node.left = self.__insert(node.left, key, priority)     # 左の子へのポインタを更新
            if node.priority < node.left.priority:                  # 左の子の方が優先度が高い場合右回転
                node = self.right_rotate(node)
        else:                                                       # 右の子へ移動
            node.right = self.__insert(node.right, key, priority)   # 右の子へポインタを更新
            if node.priority < node.right.priority:                 # 右の子の方が優先度が高い場合左回転
                node = self.left_rotate(node)
        return node

    def delete(self, key):
        target = self.delete_target(self.root, key)


    def delete_target(self, node, key):
        if node == None: return None
        if key < node.key:
            node.left = self.delete_target(self.left, key)
        elif key > node.key:
            node.right = self.delete_target(node.right, key)
        else:
            return self.__delete(node, key)
        return Node

    def __delete(self, node, key):
        if node.left == None and node.right == None:
            return None
        elif node.left == None:
            node = self.left_rotate(node)
        elif node.right == None:
            node = self.right_rotate(node)
        else:
            if node.left.priority > node.right.priority:
                node = self.right_rotate(node)
            else:
                node = self.left_rotate(node)
        return self.delete_target(node, key)

    def find(self, key):
        pass

    # 先行順巡回
    def preorder(self):
        self.preorder_list = []
        self.__preorder_bfs(self.root)
        return self.preorder_list

    def __preorder_bfs(self, u):
        if u == None: return
        self.preorder_list.append(u.val)
        self.__preorder_bfs(u.left)
        self.__preorder_bfs(u.right)

    # 中間順巡回
    def inorder(self):
        self.inorder_list = []
        self.__inorder_dfs(self.root)
        return self.inorder_list

    def __inorder_dfs(self, u):
        if u == None: return
        self.__inorder_dfs(u.left)
        self.inorder_list.append(u.val)
        self.__inorder_dfs(u.right)

def print_elements(arr):
    print(' ' + ' '.join([str(item) for item in arr]))

treap = Treap()

q = int(input())
for i in range(q):
    op, *x = list(map(int, input().split(' ')))
    if op == 'insert':
        treap.insert(x[0], x[1])
    elif op == 'find':
        treap.find(x[0])
    elif op == 'delete':
        treap.delete(x[0])
    else:
        print_elements(treap.inorder())
        print_elements(treap.preorder())
