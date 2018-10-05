#! python3
# reconstruction_of_a_tree.py

n = int(input())
preorder = list(map(int, input().split(' ')))
inorder = list(map(int, input().split(' ')))
postorder = []
pos = 0

def solve():
    global pos
    pos = 0
    reconstruction(0, len(preorder))
    for i in range(n):
        if i: print(' ', end='')
        print(postorder[i], end='')
    print()

def reconstruction(left, right):
    global inorder, preorder, postorder, pos
    if left >= right: return None
    root = preorder[pos]
    pos += 1
    mid = inorder.index(root)
    reconstruction(left, mid)
    reconstruction(1 + mid, right)
    postorder.append(root)

solve()
