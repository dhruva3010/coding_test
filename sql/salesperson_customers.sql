SELECT s.name AS salesman_name, c.cust_name AS customer_name
FROM Salesman s
JOIN Customer c ON s.salesman_id = c.salesman_id
WHERE s.city = 'London' AND c.city = 'London'
