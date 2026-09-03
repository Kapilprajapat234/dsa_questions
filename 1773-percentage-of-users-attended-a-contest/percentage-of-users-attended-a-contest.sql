SELECT re.contest_id,
       ROUND(COUNT(re.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register AS re
GROUP BY re.contest_id
ORDER BY percentage DESC, re.contest_id ASC;