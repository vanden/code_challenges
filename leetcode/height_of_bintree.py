# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    levelCount = -1
    toExplore = [root]
    while toExplore:
        levelCount += 1
        current = toExplore
        toExplore = []
        for node in current:
            toExplore.extend([n for n in (node.left, node.right) if n])
    return levelCount
