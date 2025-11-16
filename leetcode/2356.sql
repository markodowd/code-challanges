-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM
    Teacher
GROUP BY
    teacher_id;

