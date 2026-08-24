# Write your MySQL query statement below
SELECT em.name 
FROM Employee as e
JOIN Employee as em
ON  e.managerId = em.id
WHERE e.managerId is not null  
GROUP BY em.id , em.name
HAVING count(e.managerId)  >= 5 ; 