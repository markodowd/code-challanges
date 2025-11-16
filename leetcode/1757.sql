-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y'
    AND recylable = 'Y';

