class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def array_to_binary_tree(arr, index=0):
        if index < len(arr):
            if arr[index] is None:
                return None
            root = TreeNode(arr[index])
            root.left = TreeNode.array_to_binary_tree(arr, 2 * index + 1)
            root.right = TreeNode.array_to_binary_tree(arr, 2 * index + 2)
            return root
        return None

    @staticmethod
    def isSameTree(p, q) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        if TreeNode.isSameTree(p.left, q.left) == False:
            return False

        if TreeNode.isSameTree(p.right, q.right) == False:
            return False
        return p.val == q.val
