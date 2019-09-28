import copy


class AstNode:
    
    def __init__(self, operator, sub_exp=None):
        self.operator = operator  # save t, f, !, |, &
        self.sub_exp = sub_exp


class Solution:

    def get_sub_expression(self, expression):
        """
            parse '(&(t,f,t),!(t))' => ['&(t,f,t)', '!(t)']
        """

        stack = []
        tmp = []
        res = []
        
        for ch in expression:
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                stack.pop()
            
            if len(stack) == 1 and ch == ',':
                res.append(''.join(copy.deepcopy(tmp)))
                tmp = []
                continue
            if len(stack) == 1 and ch == '(':
                continue
            if len(stack) == 0 and ch == ')':
                continue
            tmp.append(ch)
        if tmp:
            res.append(''.join(copy.deepcopy(tmp)))
        return res
    
    def generate_ast(self, exp):
        if exp[0] == 't':
            return AstNode('t')
        elif exp[0] == 'f':
            return AstNode('f')
        else:
            root = AstNode(exp[0], [])
            sub_exp = self.get_sub_expression(exp[1:]) 
            for se in sub_exp:
                root.sub_exp.append(self.generate_ast(se))
            return root
    
    def parse_ast(self, root):
        if not root.sub_exp:
            return True if root.operator == 't' else False
        elif root.operator == '!':
            return not self.parse_ast(root.sub_exp[0])
        elif root.operator == '|':
            for se in root.sub_exp:
                if self.parse_ast(se):
                    return True
            return False
        elif root.operator == '&':
            for se in root.sub_exp:
                if not self.parse_ast(se):
                    return False 
            return True 

    def parse_bool_expression(self, exp):
        ast = self.generate_ast(exp)
        return self.parse_ast(ast)
        

if __name__ == '__main__':
    cases = [
        '!(f)',
        '|(f,t)',
        '&(t,f)',
        "|(&(t,f,t),!(t))",
    ]
    obj = Solution()
    for exp in cases:
        res = obj.parse_bool_expression(exp)
        print(res)
