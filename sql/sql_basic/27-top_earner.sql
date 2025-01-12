SELECT AVG(months*salary), count(employee_id)
FROM Employee 
WHERE months*salary=(
    select max(months*salary) FROM Employee
);