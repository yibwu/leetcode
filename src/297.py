# Definition for a binary tree node.
# class TreeNode(object):
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
        queue = [[root, -1, -1]]
        while queue:
            tmp = queue.pop(0)
            cur, parentIdx, direction = tmp[0], tmp[1], tmp[2]
            arr.append([cur.val, parentIdx, direction])
            if cur.left:
                queue.append([cur.left, len(arr)-1, 0])
            if cur.right:
                queue.append([cur.right, len(arr)-1, 1])
        return json.dumps(arr)
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = json.loads(data)
        if not arr:
            return None
        
        i = 0
        while i < len(arr):
            val, parentIdx, direction = arr[i][0], arr[i][1], arr[i][2]
            arr[i][0] = TreeNode(val)
            if parentIdx != -1:
                parent = arr[parentIdx][0]
                if direction == 0:
                    parent.left = arr[i][0]
                else:
                    parent.right = arr[i][0]
            i += 1
        return arr[0][0]
 
