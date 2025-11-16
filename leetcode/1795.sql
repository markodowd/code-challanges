-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

/*
Author: Mark O'Dowd
Email: contact@markodowd.dev
LeetCode: https://leetcode.com/u/markodowd
 */
SELECT
    product_id,
    s.store,
    s.price
FROM
    products p
    CROSS JOIN LATERAL unnest(ARRAY['store1', 'store2', 'store3'], ARRAY[p.store1, p.store2, p.store3]) AS s (store,
        price)
WHERE
    s.price IS NOT NULL;

