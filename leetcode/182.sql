-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

SELECT
    email AS "Email"
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(email) > 1;

