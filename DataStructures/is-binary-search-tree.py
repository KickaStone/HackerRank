""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
# def dfs(root, arr):
#     if root:
#         dfs(root.left, arr)
#         arr.append(root.data)
#         dfs(root.right, arr)

# def check_binary_search_tree_(root):
#     arr = []
#     dfs(root, arr)
#     for i in range(1, len(arr)):
#         if arr[i] <= arr[i-1]:
#             return False
#     return True

last = -1

def check_binary_search_tree_(root):
    """
    The in-order traversal of a binary search tree should be sorted.
    """
    if root:
        left = check_binary_search_tree_(root.left)
        global last
        # print('root={}, last={}'.format(root.data, last))
        if root.data <= last:
            return False
        last = root.data
        right = check_binary_search_tree_(root.right)
        return left and right
    else:
        return True