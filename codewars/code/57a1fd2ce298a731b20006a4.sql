SELECT
    str,
    CASE WHEN LOWER(str) = REVERSE(LOWER(str)) THEN
        TRUE
    ELSE
        FALSE
    END AS res
FROM
    ispalindrome;

