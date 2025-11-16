-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM
    Employees
GROUP BY
    event_day,
    emp_id;

