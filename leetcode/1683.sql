-- Author: Mark O'Dowd
-- Email: contact@markodowd.dev
-- LeetCode: https://leetcode.com/u/markodowd

/*
Author: Mark O'Dowd
Email: contact@markodowd.dev 
LeetCode: https://leetcode.com/u/markodowd
 */
SELECT
    tweet_id
FROM
    Tweets
WHERE
    LENGTH(content) > 15;

