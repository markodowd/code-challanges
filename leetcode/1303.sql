-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

SELECT 
    employee_id, 
    COUNT(*) OVER (PARTITION BY team_id) as team_size 
FROM Employee;

