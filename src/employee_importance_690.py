# Employee info
class Employee:

    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    
    def get_importance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        id_employee = dict()
        for e in employees:
            id_employee[e.id] = e 
          
        ids = set()
        importance = [0]
        self.dfs(id_employee[id], importance, id_employee, ids)
        return importance[0]
    
    def dfs(self, employee, importance, id_employee, ids):
        if employee.id not in ids:
            ids.add(employee.id)
            importance[0] += employee.importance
        for s in employee.subordinates:
            self.dfs(id_employee[s], importance, id_employee, ids)
        

if __name__ == '__main__':
    employees = [
        Employee(1, 5, [2, 3]),    
        Employee(2, 3, []),    
        Employee(3, 3, []),    
    ]
    obj = Solution()
    print(obj.get_importance(employees, 1))
