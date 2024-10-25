SELECT e.first_name, e.last_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE e.manager_id IS NOT NULL
AND l.country_id = 'USA'
