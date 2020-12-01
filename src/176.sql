SELECT CASE
           WHEN count(*) > 0 THEN Salary
       END AS SecondHighestSalary
FROM
   (SELECT distinct(Salary)
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1
    OFFSET 1) tmp;
