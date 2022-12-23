select FIRST_NAME< LAST_NAME from 
(   
    (((select FIRST_NAME, LAST_NAME, MANAGER_ID from employees) e
    left join
    (select MANAGER_ID, LOCATION_ID from departments) d
    on 
    e.MANAGER_ID = d.MANAGER_ID) ed
    left join
    select LOCATION_ID, country_id from locations l
    on 
    l.LOCATION_ID, ed.LOCATION_ID)  
) res
where res.country_id = 'US' and (MANAGER_ID is not null and MANAGER_ID != '')