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
        for item in employees:
            id_employee[item.id] = item
          
        id_set = set()
        importance = [id_employee[id].importance]
        subordinates = id_employee[id].subordinates
        id_set.add(id)

        for s in subordinates:
            if s not in id_set:
                self.dfs(id_employee[s], importance, id_employee, id_set)
        return importance[0]
    
    def dfs(self, employee, importance, id_employee, id_set):
        if employee.id not in id_set:
            id_set.add(employee.id)
            importance[0] += employee.importance
        for s in employee.subordinates:
            self.dfs(id_employee[s], importance, id_employee, id_set)
        

if __name__ == '__main__':
    employees = [
        Employee(1, 5, [2, 3]),    
        Employee(2, 3, []),    
        Employee(3, 3, []),    
    ]
    obj = Solution()
    print(obj.get_importance(employees, 1))
