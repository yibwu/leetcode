# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return json.dumps([])
        
        arr = []
        queue = [[root, -1]]
        while queue:
            tmp = queue.pop(0)
            cur, parentIdx = tmp[0], tmp[1]
            arr.append([cur.val, parentIdx])
            if cur.left:
                queue.append([cur.left, len(arr)-1])
            if cur.right:
                queue.append([cur.right, len(arr)-1])
        return json.dumps(arr)
 
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = json.loads(data)
        if not arr:
            return None
        
        i = 0
        while i < len(arr):
            val, parentIdx = arr[i][0], arr[i][1]
            arr[i][0] = TreeNode(val)
            if parentIdx != -1:
                parent = arr[parentIdx][0]
                if parent.val > val:
                    parent.left = arr[i][0]
                else:
                    parent.right = arr[i][0]
            i += 1
        return arr[0][0]
 
