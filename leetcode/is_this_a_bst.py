# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if not root:
        return True
    inOrderNodes = inOrderTraversal(root)
    vals = [n.data for n in inOrderNodes]
    # Problem spec has it that for a BST all vals unique
    return vals == sorted(vals) and len(vals) == len(set(vals))

def inOrderTraversal(root):
    if not root:
        return []
    result = inOrderTraversal(root.left)
    result.append(root)
    result.extend(inOrderTraversal(root.right))
    return result
        
