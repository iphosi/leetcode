from collections import deque


# data = [1, 2, 3, None, None, 4, 5]
# node 索引为 n
# node.val 不为 None 时，node.left 索引为 2 * (n - m) + 1，node.right 索引为 2 * (n - m) + 2


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[]"

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            node = queue.popleft()
            if node is not None:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")

        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        vals = data[1:-1].split(',')
        i = 1
        root = TreeNode(int(vals[0]))

        queue = deque()
        queue.append(root)

        while queue and i < len(vals):
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root
