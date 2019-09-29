class AstNode:
    
    def __init__(self, operator, sub_exp=None):
        self.operator = operator  # save t, f, !, |, &
        self.sub_exp = sub_exp


class Solution:
    OP_TRUE = 't'
    OP_FALSE = 'f'
    OP_NOT = '!'
    OP_OR = '|'
    OP_AND = '&'

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
                res.append(''.join(tmp))
                tmp = []
                continue
            if len(stack) == 1 and ch == '(':
                continue
            if len(stack) == 0 and ch == ')':
                continue
            tmp.append(ch)
        if tmp:
            res.append(''.join(tmp))
        return res
    
    def generate_ast(self, exp):
        if exp[0] == self.OP_TRUE:
            return AstNode(self.OP_TRUE)
        elif exp[0] == self.OP_FALSE:
            return AstNode(self.OP_FALSE)
        else:
            root = AstNode(exp[0], [])
            sub_exp = self.get_sub_expression(exp[1:]) 
            for se in sub_exp:
                root.sub_exp.append(self.generate_ast(se))
            return root
    
    def parse_ast(self, root):
        if not root.sub_exp:
            return True if root.operator == self.OP_TRUE else False
        elif root.operator == self.OP_NOT:
            return not self.parse_ast(root.sub_exp[0])
        elif root.operator == self.OP_OR:
            for se in root.sub_exp:
                if self.parse_ast(se):
                    return True
            return False
        elif root.operator == self.OP_AND:
            for se in root.sub_exp:
                if not self.parse_ast(se):
                    return False 
            return True 

    def parse_bool_expression(self, exp):
        ast = self.generate_ast(exp)
        return self.parse_ast(ast)
        

if __name__ == '__main__':
    cases = [
        '!f',
        '!(f)',
        '|(f,t)',
        '&(t,f)',
        "|(&(t,f,t),!(t))",
    ]
    obj = Solution()
    for exp in cases:
        res = obj.parse_bool_expression(exp)
        print(res)
