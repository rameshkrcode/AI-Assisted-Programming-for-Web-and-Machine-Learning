SELECT employee_id, first_name, last_name, department, salary
FROM employees
WHERE department = 'IT' AND salary > 80000
ORDER BY salary DESC;