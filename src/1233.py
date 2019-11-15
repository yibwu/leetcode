class Solution(object):
    
    def insert(self, root, path):
        paths = path.split('/')[1:]
        r = root
        for p in paths:
            if p not in r:
                r[p] = dict()
            r = r[p]
        r['end'] = path
            
    def remove_subfolders(self, folder):
        root = dict()
        for f in folder:
            self.insert(root, f)
        
        res = []
        self.visit(root, res)
        return res
        
    def visit(self, root, res):
        if 'end' not in root:
            for k in root.keys():
                self.visit(root[k], res)
        else:
            res.append(root['end'])


if __name__ == '__main__':
    cases = [
        ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"],
        ["/a", "/a/b/c", "/a/b/d"],
        ["/a/b/c", "/a/b/ca", "/a/b/d"],
    ]
    obj = Solution()
    for c in cases:
        res = obj.remove_subfolders(c)
        print(c, res)
