# Write your MySQL query statement below
select po.project_id , 
round(avg(experience_years) , 2 ) as average_years 
from project  as po 
left join employee as em 
on po.employee_id = em.employee_id 
group by po.project_id ;
