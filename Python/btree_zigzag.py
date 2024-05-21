"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between)
"""

from collections import deque

class BTreeNode:
  """
  Binary tree node class
  """
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.count = 1

  def insert(self, value):
    if value < self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BTreeNode(value)
    elif value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BTreeNode(value)
    else:
      self.count += 1

  def zigzag(self):
    # Do a zig-zag level traversal from this node
    visited = []
    explored = deque([self])
    d = 0
    while explored:
      level = deque()
      l = len(explored)
      for _ in range(l):
        node = explored.popleft()
        if d % 2 == 0:
          level.extendleft([node.value]*node.count)
        else:
          level.extend([node.value]*node.count)

        if node.left:
          explored.append(node.left)
        if node.right:
          explored.append(node.right)
      
      visited.extend(level)
      d += 1
    
    return visited
      
  def inorder(self):
    def helper(node):
      if node.left:
        helper(node.left)
      print(f"{node.value} "*node.count, end="")
      if node.right:
        helper(node.right)
    
    return helper(self)

  def __repr__(self):
    return f"{self.value}"


def main():
  tree = BTreeNode(5) # initialize root
  keys = [3, 7, 2, 4, 6, 2, 8, 8, 1, 0, 9]
  for key in keys:
    tree.insert(key)

  print("----Begin inorder traversal----")
  tree.inorder()
  print("\n")
  print("----Begin ZigZag order traversal----")
  print(tree.zigzag())
  print("------------------------------------")


if __name__ == "__main__":
  main()