class Node:
    def __init__(self, num):
        self.num = num
        self.children = []


def tree(node: Node):
    if node.children.len() < 1: return
    for i in node.children:
      tree(node.children[i])
