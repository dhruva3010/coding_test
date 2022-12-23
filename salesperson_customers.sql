select * from (
    (select * from salesman) s
    left join 
    (select * from customers) c
    on s.salesman_id = c.salesman_id and s.city = c.city
) res
where res.city = 'London'