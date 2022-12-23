select FIRST_NAME, LAST_NAME, salary from (
    select FIRST_NAME, LAST_NAME, salary, AVG(salary) average_salary from (
    (select FIRST_NAME, LAST_NAME, salary from employees) e 
    left join
    (select DEPARTMENT_ID, DEPARTMENT_NAME from departments
    where DEPARTMENT_NAME = 'IT') d
    on e.DEPARTMENT_ID = d.DEPARTMENT_ID
    )
) res
where res.salary > res.average_salary
